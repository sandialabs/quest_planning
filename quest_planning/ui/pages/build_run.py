from PySide6.QtCore import QObject, QRunnable, QThreadPool, QTimer, Signal, Slot
from PySide6.QtWidgets import QFileDialog, QWidget
from pathlib import Path
import traceback

from quest_planning.ui.forms.execute_model.ui_execute_model import (
    Ui_ExecuteModelPage,
)
from quest_planning.ui.utils.help_topics import show_error, show_help
from quest_planning.ui.utils.splash import ExecuteModelSplash
from quest_planning.paths import BASE_DIR


class WorkerSignals(QObject):
    """Signals emitted by a model operation running in a worker thread."""

    finished = Signal(object)
    error = Signal(str)


class Worker(QRunnable):
    """Run a callable in the page's thread pool and report its outcome."""

    def __init__(self, function):
        super().__init__()
        self.function = function
        self.signals = WorkerSignals()

    @Slot()
    def run(self):
        try:
            result = self.function()
        except Exception as exc:
            details = "{}: {}\n\n{}".format(
                type(exc).__name__, exc, traceback.format_exc()
            )
            self.signals.error.emit(details)
        else:
            self.signals.finished.emit(result)


class ExecuteModelPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ExecuteModelPage()
        self.ui.setupUi(self)

        self.setObjectName("execute_model_page")

        self.ui.model_status_frame.setHidden(True)

        self.ui.browse_folder_button.setToolTip(
            "Browse for the folder where the results will be saved."
        )
        self.ui.build_button.setToolTip("Build the optimization model.")
        self.ui.run_button.setToolTip("Solve the optimization model.")
        self.ui.btn_model_help.setToolTip("Help: build and solve the model.")
        self.ui.solver_select_box.setToolTip(
            "Select the solver installed on this machine."
        )

        self.ui.browse_folder_button.clicked.connect(self.select_file)
        self.ui.build_button.clicked.connect(self.on_build_button_clicked)
        self.ui.run_button.clicked.connect(self.on_run_button_clicked)
        self.ui.btn_model_help.clicked.connect(
            lambda: show_help(self, "Build & Solve Optimization Model")
        )
        self.data_handler = None
        self.optimizer = None
        self.results_viewer = None
        self.scenario_page = None
        self.splash = None
        self.threadpool = QThreadPool(self)
        self._active_worker = None

    def set_model_flow(self, data_handler, optimizer, scenario_page, results_viewer=None):
        """Connect this page to the application's shared model objects."""
        self.data_handler = data_handler
        self.optimizer = optimizer
        self.scenario_page = scenario_page
        self.results_viewer = results_viewer

    def select_file(self):
        results_dir = BASE_DIR / "Results"
        selected_dir = QFileDialog.getExistingDirectory(
            self,
            "Select Results Folder",
            str(results_dir),
        )
        if not selected_dir:
            return

        if self.ui.results_file_box.findText(selected_dir) == -1:
            self.ui.results_file_box.addItem(selected_dir)
        self.ui.results_file_box.setCurrentText(selected_dir)

    def update_output_box(self, text):
        self.ui.report_progress_box.appendPlainText(str(text))

    def _build_model_inputs(self):
        """Apply the selected scenario and prepare load blocks on the GUI thread."""
        if self.scenario_page is None:
            raise RuntimeError("Scenario Builder is not connected.")
        if self.data_handler is None:
            raise RuntimeError("The data handler is not connected.")

        if not self.data_handler.load_data:
            raise RuntimeError("Load a power system dataset before building the model.")

        required_tables = {
            "branch",
            "bus",
            "capex_es",
            "capex_tech",
            "fuel",
            "gen",
            "load",
            "policy",
            "scalars",
            "solar",
            "solar_cand",
            "storage",
            "tech",
            "wind",
            "wind_cand",
        }
        loaded_tables = set(self.data_handler.data_ls or ())
        missing_tables = required_tables.difference(loaded_tables)
        if missing_tables:
            missing = ", ".join(sorted(missing_tables))
            raise RuntimeError(f"Dataset is missing required tables: {missing}.")

        solver_label = self.ui.solver_select_box.currentText().strip()
        solver_names = {
            "Clp": "clp",
            "GLPK": "glpk",
            "Gurobi": "gurobi",
            "HiGHs": "HiGHs",
        }
        if solver_label not in solver_names:
            raise RuntimeError("Select a supported solver before running the model.")

        self.data_handler.set_solver(solver_names[solver_label])
        self.optimizer.solver = self.data_handler.solver

        self.scenario_page.apply_scenario_to_data_handler()
        self._complete_policy_schedule()
        self.scenario_page.apply_large_loads_to_data_handler()
        self.data_handler.construct_load_blocks()

    def _complete_policy_schedule(self):
        """Fill policy years absent from the dataset using nearest schedule values."""
        policy_key = self.data_handler.index("policy")
        policy = self.data_handler.load_data[policy_key]
        if "Years" not in policy.columns:
            raise RuntimeError("The policy table must contain a Years column.")

        policy = policy.copy()
        policy["Years"] = policy["Years"].astype(int)
        policy = policy.drop_duplicates("Years", keep="last").set_index("Years")
        modeled_years = {int(year) for year in self.data_handler.years}
        all_years = sorted(set(policy.index).union(modeled_years))
        policy = policy.reindex(all_years)

        policy_columns = ("RPS", "CO2", "CO2_intensity")
        for column in policy_columns:
            if column not in policy.columns:
                raise RuntimeError(
                    "The policy table is missing the {} column.".format(column)
                )
            policy[column] = policy[column].ffill().bfill()
            if policy.loc[sorted(modeled_years), column].isna().any():
                raise RuntimeError(
                    "The policy table has no usable values for {}.".format(column)
                )

        policy.index.name = "Years"
        self.data_handler.load_data[policy_key] = policy.reset_index()

    def _start_worker(self, function, on_success, on_error):
        worker = Worker(function)
        worker.signals.finished.connect(on_success)
        worker.signals.error.connect(on_error)
        self._active_worker = worker
        self.threadpool.start(worker)

    def on_build_button_clicked(self):
        """Prepare scenario inputs before optimization, on the GUI thread."""
        try:
            if self.optimizer is None:
                raise RuntimeError("The optimizer is not connected.")
            self._build_model_inputs()
        except Exception as exc:
            traceback.print_exc()
            self.ui.model_status_frame.setHidden(False)
            self.ui.label_status_desc.setText("Model input preparation failed.")
            show_error(
                self,
                "Build Model Failed",
                "{}: {}. See the console traceback for the failing operation.".format(
                    type(exc).__name__, exc
                ),
            )
            return False
        self.ui.model_status_frame.setHidden(False)
        self.ui.label_status_desc.setText("Model inputs are ready.")
        self.update_output_box("Model input preparation completed.")
        return True

    def _run_and_save_results(self, output_root):
        """Solve the model and save its result structure under the chosen folder."""
        result = self.optimizer.run()
        if self.results_viewer is None:
            raise RuntimeError("The results processor is not connected.")

        output_path = Path(output_root).expanduser()
        result_vars, result_params, timestamp = result
        self.results_viewer.process_results_gui(
            result_vars,
            result_params,
            timestamp,
            self.optimizer.report,
            str(output_path),
        )
        return result

    def on_run_button_clicked(self):
        if self._active_worker is not None:
            return
        if self.optimizer is None:
            show_error(self, "Solve Model", "The optimizer is not connected.")
            return

        # This stage reads page state and updates the shared data handler, so it
        # stays on the GUI thread. The optimizer solve runs in the worker.
        if not self.on_build_button_clicked():
            return

        output_root = self.ui.results_file_box.currentText().strip()
        if not output_root:
            output_root = str(BASE_DIR / "Results")
        output_path = Path(output_root).expanduser()
        if not output_path.is_dir():
            show_error(self, "Results Folder", "Select an existing Results folder before solving.")
            return

        self.splash = ExecuteModelSplash(self)
        self.splash.set_status("Building and solving the optimization model...")
        self.splash.set_progress(None)
        self.ui.run_button.setEnabled(False)
        self.ui.build_button.setEnabled(False)
        self.splash.show()
        self.splash.raise_()

        self._start_worker(
            lambda: self._run_and_save_results(str(output_path)),
            self._on_solve_finished,
            self._on_solve_failed,
        )

    @Slot(object)
    def _on_solve_finished(self, _result):
        self._active_worker = None
        self.ui.run_button.setEnabled(True)
        self.ui.build_button.setEnabled(True)
        self.splash.set_status("Simulation complete.")
        self.splash.set_progress(100)
        QTimer.singleShot(700, self.splash.close)

    @Slot(str)
    def _on_solve_failed(self, message):
        self._active_worker = None
        self.ui.run_button.setEnabled(True)
        self.ui.build_button.setEnabled(True)
        self.splash.close()
        self.splash = None
        show_error(self, "Solve Model Failed", message)
