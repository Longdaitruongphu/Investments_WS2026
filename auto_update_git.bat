@echo off
setlocal
cd /d "%~dp0"
powershell.exe -ExecutionPolicy Bypass -NoProfile -File "%~dp0auto_update_git.ps1"
endlocal
