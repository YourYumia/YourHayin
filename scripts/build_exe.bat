@echo off
setlocal

cd /d "%~dp0.."

python -m pip install --upgrade -r src\requirements.txt
if errorlevel 1 (
    echo.
    echo Failed to install the project requirements.
    pause
    exit /b 1
)

python -m PyInstaller --onefile ^
  --icon=src\ourdream.ico ^
  --add-data "src\ourdream.ico;." ^
  --add-data "src\qdb.json;." ^
  --collect-all customtkinter ^
  --name YourHayin ^
  src\app.py

if errorlevel 1 (
    echo.
    echo Build failed - check the output above.
    echo If it reports Access is denied, close all running YourHayin.exe instances and retry.
    pause
    exit /b 1
)

if exist dist\YourHayin.exe (
    echo.
    echo Build complete: dist\YourHayin.exe
) else (
    echo.
    echo Build failed - check the output above.
    pause
    exit /b 1
)

pause
cls