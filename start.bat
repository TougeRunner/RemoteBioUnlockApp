@echo off
title RemoteBioUnlock Server
echo ==================================================
echo   RemoteBioUnlock Server
echo   Starting...
echo ==================================================

cd /d "%~dp0" REM #sets the current directory to the location of this batch file, so it can be run from anywhere without issues
python server.py
pause