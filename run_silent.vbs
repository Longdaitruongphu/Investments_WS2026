' Script chạy ngầm auto_update_git.ps1 không hiện cửa sổ cmd hay PowerShell
Set fso = CreateObject("Scripting.FileSystemObject")
currentDir = fso.GetParentFolderName(WScript.ScriptFullName)
ps1Path = currentDir & "\auto_update_git.ps1"

Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "powershell.exe -ExecutionPolicy Bypass -NoProfile -WindowStyle Hidden -File """ & ps1Path & """", 0, False
