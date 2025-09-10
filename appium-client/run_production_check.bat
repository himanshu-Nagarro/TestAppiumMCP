@echo off
echo Running INDITEX Production Check validation test...
python run_production_check.py %*
if %ERRORLEVEL% NEQ 0 (
  echo Test failed! Check logs for details.
  exit /b %ERRORLEVEL%
)
echo Test completed successfully!