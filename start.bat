@echo off
cd /d "%~dp0"
where py >nul 2>nul
if not errorlevel 1 goto pylaunch
where python >nul 2>nul
if not errorlevel 1 goto pythonlaunch
echo Python 3 is required. Install Python and try again.
pause
exit /b 1
:pylaunch
py -3 launch.py
pause
exit /b
:pythonlaunch
python launch.py
pause
