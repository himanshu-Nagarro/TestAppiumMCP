@echo off
REM Inditex Login Automation - Windows Batch Runner
REM This script provides easy access to run the Inditex login automation

echo.
echo ==========================================
echo    Inditex Login Automation Runner
echo ==========================================
echo.

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.7+ and try again
    pause
    exit /b 1
)

REM Show menu
:menu
echo Please select an option:
echo.
echo 1. Run automation with config credentials
echo 2. Run automation with custom credentials
echo 3. Run test suite
echo 4. Check prerequisites
echo 5. Install dependencies
echo 6. Exit
echo.
set /p choice="Enter your choice (1-6): "

if "%choice%"=="1" goto run_basic
if "%choice%"=="2" goto run_custom
if "%choice%"=="3" goto run_tests
if "%choice%"=="4" goto check_prereq
if "%choice%"=="5" goto install_deps
if "%choice%"=="6" goto exit
echo Invalid choice. Please try again.
goto menu

:run_basic
echo.
echo Running automation with configuration file credentials...
python run_automation.py
goto end

:run_custom
echo.
set /p email="Enter email: "
set /p password="Enter password: "
echo.
echo Running automation with custom credentials...
python run_automation.py -e "%email%" -p "%password%"
goto end

:run_tests
echo.
echo Running test suite...
python run_automation.py --test
goto end

:check_prereq
echo.
echo Checking prerequisites...
python run_automation.py --check
goto end

:install_deps
echo.
echo Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies
) else (
    echo Dependencies installed successfully!
)
goto end

:exit
echo.
echo Goodbye!
exit /b 0

:end
echo.
echo Press any key to return to menu or Ctrl+C to exit...
pause >nul
goto menu
