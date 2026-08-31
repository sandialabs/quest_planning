@echo off
setlocal

REM ========================================
REM Python version
REM ========================================
set PYTHON_EXE=py -3.11

REM ========================================
REM Paths
REM ========================================
set VENV_PATH=%~dp0env_progress
set REPO_PATH=%VENV_PATH%\snl-progress

REM ========================================
REM Remove existing virtual environment
REM ========================================
if exist "%VENV_PATH%" (
    echo Removing existing virtual environment...
    rmdir /S /Q "%VENV_PATH%"
)

REM ========================================
REM Create virtual environment
REM ========================================
echo Creating Python 3.11 virtual environment...
%PYTHON_EXE% -m venv "%VENV_PATH%"

if errorlevel 1 (
    echo ERROR: Failed to create virtual environment
    exit /b 1
)

REM ========================================
REM Activate virtual environment
REM ========================================
call "%VENV_PATH%\Scripts\activate.bat"

REM ========================================
REM Upgrade pip
REM ========================================
echo Upgrading pip...
python -m pip install --upgrade pip

REM ========================================
REM Clone ProGRESS repository
REM ========================================
echo Cloning ProGRESS repository...

git clone -b main https://github.com/sandialabs/snl-progress.git "%REPO_PATH%"

if errorlevel 1 (
    echo ERROR: Failed to clone ProGRESS repository
    exit /b 1
)

REM ========================================
REM Install requirements.txt
REM ========================================
echo Installing ProGRESS requirements...

python -m pip install -r "%REPO_PATH%\requirements.txt"

if errorlevel 1 (
    echo ERROR: Failed to install requirements
    exit /b 1
)

REM ========================================
REM Add progress folder to Python path
REM ========================================
echo Adding ProGRESS module to virtual environment...

for /f "delims=" %%i in ('python -c "import site; print(site.getsitepackages()[0])"') do (
    set SITE_PACKAGES=%%i
)

echo %REPO_PATH%>"%SITE_PACKAGES%\snl_progress.pth"

REM ========================================
REM Test import
REM ========================================
echo Testing ProGRESS import...

python -c "import progress; print('ProGRESS found at:', progress.__file__)"

if errorlevel 1 (
    echo ERROR: Could not import progress
    exit /b 1
)

REM ========================================
REM Finish
REM ========================================
deactivate

echo.
echo ========================================
echo ProGRESS setup complete successfully.
echo ========================================

endlocal
exit /b 0