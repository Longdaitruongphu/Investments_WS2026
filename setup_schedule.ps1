# Script thiet lap Windows Task Scheduler chay luc 23:59 (11:59 PM) hang ngay
$taskName = "Investments_Daily_Git_Update"
$oldTaskName = "Antigravity_Git_Update_Investments"
$workingDir = "d:\Downloads\Investments_WS2026"
$vbsPath = "$workingDir\run_silent.vbs"
$wscriptPath = "$env:SystemRoot\System32\wscript.exe"

Write-Host "Dang thiet lap lich tu dong cap nhat bai hoc..." -ForegroundColor Cyan

# Xoa task cu neu co
Unregister-ScheduledTask -TaskName $oldTaskName -Confirm:$false -ErrorAction SilentlyContinue
Unregister-ScheduledTask -TaskName $taskName -Confirm:$false -ErrorAction SilentlyContinue

# Tao hanh dong chay silent vbs
$action = New-ScheduledTaskAction -Execute $wscriptPath -Argument "`"$vbsPath`"" -WorkingDirectory $workingDir

# Tao trigger 23:59 (11:59 PM) moi ngay
$trigger = New-ScheduledTaskTrigger -Daily -At "23:59"

# Cai dat quan trong:
# - Cho phep chay khi dung pin (AllowStartIfOnBatteries)
# - Khong dung khi chuyen sang pin (DontStopIfGoingOnBatteries)
# - Chay bu ngay khi mo may neu bo lo gio 23:59 (StartWhenAvailable)
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Hours 1)

Register-ScheduledTask `
    -TaskName $taskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -Description "Tu dong cap nhat bai hoc Investments WS2026 tu Git upstream vao 11:59 PM hang ngay."

Write-Host "Thiet lap thanh cong! Task Name: $taskName" -ForegroundColor Green
Write-Host "Gio chay: 11:59 PM (23:59) hang ngay." -ForegroundColor Green
