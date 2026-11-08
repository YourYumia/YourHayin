@echo off
setlocal

cd /d "%~dp0.."

python -m pip install --upgrade pyinstaller
if errorlevel 1 (
    echo.
    echo Failed to install or upgrade PyInstaller.
    pause
    exit /b 1
)

python -m PyInstaller --onefile ^
  --icon=src\ourdream.ico ^
  --add-data "src\ourdream.ico;." ^
  --add-data "src\qdb.json;." ^
  --collect-all plyer ^
  --hidden-import=plyer.platforms.win.notification ^
  --hidden-import=plyer.platforms.win ^
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