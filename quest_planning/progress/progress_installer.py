import argparse
import shutil
import subprocess
import sys
import logging
from dataclasses import dataclass
from pathlib import Path
from quest_planning.paths import get_path

root_dir = Path(get_path())
progress_dir = root_dir / "progress"
ProGRESS_env_dir = progress_dir / "env_progress"

class ProGRESSInstallerError(RuntimeError):
    pass

@dataclass(frozen=True)
class ProGRESSInstallCommand:
    program: str
    arguments: list[str]
    working_directory: object
    script_path: object

    def as_subprocess_args(self) -> list[str]:
        return [self.program, *self.arguments]

def get_ProGRESS_env_dir():
    return ProGRESS_env_dir

def get_ProGRESS_python_executable():
    """
    Return the expected Python executable inside the ProGRESS virtual environment.
    """
    if sys.platform.startswith("win"):
        return ProGRESS_env_dir / "Scripts" / "python.exe"

    return ProGRESS_env_dir / "bin" / "python"

def is_ProGRESS_installed() -> bool:
    """
    ProGRESS is considered installed only if the expected Python executable exists.
    """
    python_exe = get_ProGRESS_python_executable()
    return python_exe.exists() and python_exe.is_file()


def get_install_script_path():
    if sys.platform.startswith("win"):
        return progress_dir/ "install_progress.bat"

    return progress_dir / "install_progress.sh"


def get_install_command() -> ProGRESSInstallCommand:
    script_path = get_install_script_path()

    if sys.platform.startswith("win"):
        program = "cmd"
        arguments = ["/c", str(script_path)]
    else:
        program = "bash"
        arguments = [str(script_path)]

    return ProGRESSInstallCommand(
        program=program,
        arguments=arguments,
        working_directory=root_dir,
        script_path=script_path,
    )

def install_ProGRESS(*, force: bool = False, capture_output: bool = False) -> subprocess.CompletedProcess:
    """
    Install ProGRESS by running ProGRESS.bat on Windows or ProGRESS.sh on macOS/Linux.
    ProGRESS is considered installed if this directory exists:

        root_dir/env_progress
    """
    if is_ProGRESS_installed() and not force:
        raise ProGRESSInstallerError(
            f"ProGRESS is already installed at:\n{ProGRESS_env_dir}"
        )

    command = get_install_command()

    if not command.script_path.exists():
        raise ProGRESSInstallerError(
            f"ProGRESS install script not found:\n{command.script_path}"
        )

    result = subprocess.run(
        command.as_subprocess_args(),
        cwd=str(command.working_directory),
        text=True,
        capture_output=capture_output,
        check=False,
    )

    if result.returncode != 0:
        raise ProGRESSInstallerError(
            f"ProGRESS install failed with exit code {result.returncode}."
        )

    if not is_ProGRESS_installed():
        raise ProGRESSInstallerError(
            "ProGRESS install script completed, but the ProGRESS environment was not found at:\n"
            f"{ProGRESS_env_dir}"
        )

    return result

def uninstall_ProGRESS(*, missing_ok: bool = True) -> None:
    """
    Delete the ProGRESS environment at:

        root_dir/env_progress

    Includes a safety check so an unexpected path is not deleted.
    """
    if not ProGRESS_env_dir.exists():
        if missing_ok:
            return

        raise ProGRESSInstallerError(
            f"ProGRESS environment does not exist:\n{ProGRESS_env_dir}"
        )

    env_dir_resolved = ProGRESS_env_dir.resolve()
    expected_parent = (root_dir / "env_progress").resolve()

    if env_dir_resolved.name != "env_progress" or env_dir_resolved.parent != expected_parent:
        raise ProGRESSInstallerError(
            f"Refusing to delete unexpected path:\n{env_dir_resolved}"
        )
    shutil.rmtree(env_dir_resolved, onerror=remove_readonly)

def remove_readonly(func, path, exc_info):
        """
        Error handler for shutil.rmtree on Windows.
        Makes the file writable and retries the failed operation.
        """
        import os
        import stat
        os.chmod(path, stat.S_IWRITE)
        func(path)

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Install, uninstall, or check ProGRESS.")

    subparsers = parser.add_subparsers(dest="command", required=True)

    install_parser = subparsers.add_parser("install", help="Install ProGRESS.")
    install_parser.add_argument(
        "--force",
        action="store_true",
        help="Run installer even if root_dir/progress/env_progress already exists.",
    )

    subparsers.add_parser("uninstall", help="Uninstall ProGRESS.")
    subparsers.add_parser("status", help="Show ProGRESS installation status.")

    args = parser.parse_args(argv)

    try:
        if args.command == "install":
            if is_ProGRESS_installed() and not args.force:
                print(f"ProGRESS is already installed at: {ProGRESS_env_dir}")
                return 0

            print(f"Installing ProGRESS from root directory: {root_dir}")
            install_ProGRESS(force=args.force, capture_output=False)
            print(f"ProGRESS installed successfully at: {ProGRESS_env_dir}")
            return 0

        if args.command == "uninstall":
            if not is_ProGRESS_installed():
                print("ProGRESS is not installed.")
                return 0

            uninstall_ProGRESS()
            print("ProGRESS uninstalled successfully.")
            return 0

        if args.command == "status":
            if is_ProGRESS_installed():
                print(f"ProGRESS is installed at: {ProGRESS_env_dir}")
                return 0

            print("ProGRESS is not installed.")
            return 1

    except ProGRESSInstallerError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())