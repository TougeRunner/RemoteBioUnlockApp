@echo off
title RemoteBioUnlock Setup
echo ==================================================
echo   RemoteBioUnlock - First Time Setup
echo ==================================================
echo.

:: Check Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python not found. Please install Python from python.org
    echo Make sure to tick "Add Python to PATH" during installation.
    pause
    exit /b 1
)

echo [OK] Python found.
echo.

:: Install required libraries
echo [SETUP] Installing required libraries...
pip install flask cryptography pystray pillow pywin32 requests waitress

echo.
echo [OK] Libraries installed.
echo.

:: Check if config.json exists
if not exist config.json (
    echo [SETUP] Creating default config.json...
    (
        echo {
        echo     "pc_name": "My PC Name",
        echo     "secret_key": "change-this-to-something-random",
        echo     "unlock_pin": "YOUR-PIN-HERE",
        echo     "port": 5000,
        echo     "token_expiry_seconds": 30
        echo }
    ) > config.json
    echo [OK] config.json created. Please open it and fill in your details.
) else (
    echo [OK] config.json already exists. Skipping.
)

echo.
echo ==================================================
echo   Setup complete!
echo   Next steps:
echo   1. Open config.json and fill in your details
echo   2. Double click start.bat to launch the server
echo ==================================================
echo.
pause