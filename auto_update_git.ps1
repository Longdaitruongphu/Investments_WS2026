[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

$repoDir = "d:\Downloads\Investments_WS2026"
if (Test-Path $repoDir) {
    Set-Location -Path $repoDir
}

$logFile = Join-Path (Get-Location) "update_log.txt"

function Write-Log {
    param(
        [Parameter(Mandatory=$true)][string]$message,
        [Parameter(Mandatory=$false)][string]$level = "INFO"
    )
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logLine = "[$timestamp] [$level] $message"
    Write-Host $logLine
    Add-Content -Path $logFile -Value $logLine -Encoding UTF8
}

Write-Log "======================================================================" "INFO"
Write-Log "BAT DAU TIEN TRINH TU DONG CAP NHAT BAI HOC (INVESTMENTS WS2026)" "INFO"

try {
    # 1. Luu lai thay doi noi bo (local) neu co
    Write-Log "[BUOC 1] Kiem tra va tu dong luu thay doi noi bo (commit local)..." "INFO"
    git add -A 2>&1 | Out-Null
    
    $status = (git status --porcelain)
    if ($status) {
        $timeStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $commitMsg = "Auto-save local changes before daily update [$timeStr]"
        $commitResult = (git commit -m $commitMsg 2>&1 | Out-String).Trim()
        Write-Log "[BUOC 1] Phat hien thay doi local. Da commit thanh cong:`n$commitResult" "INFO"
    } else {
        Write-Log "[BUOC 1] Thu muc lam viec sach se, khong co thay doi local can commit." "INFO"
    }

    # 2. Fetch du lieu moi nhat tu upstream (DROCLB/Investments_WS2026)
    Write-Log "[BUOC 2] Dang kiem tra bai hoc moi tu upstream (DROCLB/Investments_WS2026)..." "INFO"
    $fetchResult = (git fetch upstream main 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) {
        Write-Log "[BUOC 2] Khong the tai tu upstream. Vui long kiem tra mang:`n$fetchResult" "ERROR"
    } else {
        $newCommits = (git rev-list HEAD..upstream/main --count 2>$null)
        if ($newCommits) {
            $newCommits = $newCommits.Trim()
        } else {
            $newCommits = "0"
        }

        if ([int]$newCommits -gt 0) {
            Write-Log "[BUOC 2] Phat hien $newCommits bai hoc/commit moi tu giang vien! Dang merge..." "INFO"
            $timeStr = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
            $mergeMsg = "Auto-merge daily upstream updates [$timeStr]"
            $mergeResult = (git merge upstream/main -m $mergeMsg 2>&1 | Out-String).Trim()

            if ($LASTEXITCODE -eq 0) {
                Write-Log "[BUOC 2] Da cap nhat bai hoc moi thanh cong!`n$mergeResult" "SUCCESS"
            } else {
                Write-Log "[BUOC 2] Xung dot khi merge bai hoc! Dang abort de bao ve file local:`n$mergeResult" "WARNING"
                git merge --abort 2>&1 | Out-Null
                Write-Log "[BUOC 2] Da rollback ve trang thai an toan. Vui long mo VS Code de kiem tra." "WARNING"
            }
        } else {
            Write-Log "[BUOC 2] Kho bai hoc da o ban moi nhat, khong co bai giang moi." "INFO"
        }
    }

    # 3. Dong bo toan bo len GitHub ca nhan (origin/main)
    Write-Log "[BUOC 3] Dang sao luu toan bo len GitHub ca nhan (origin/main)..." "INFO"
    $pushResult = (git push origin main 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -eq 0) {
        Write-Log "[BUOC 3] Da sao luu len GitHub ca nhan thanh cong!`n$pushResult" "SUCCESS"
    } else {
        Write-Log "[BUOC 3] Chua the push len origin (co the offline hoac khong co thay doi):`n$pushResult" "WARNING"
    }

} catch {
    Write-Log "Loi ngoai le trong qua trinh cap nhat: $($_.Exception.Message)" "ERROR"
}

Write-Log "TIEN TRINH CAP NHAT HOAN TAT AN TOAN." "INFO"
Write-Log "======================================================================`n" "INFO"
