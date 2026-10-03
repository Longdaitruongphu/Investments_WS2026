@echo off
echo [%date% %time%] Bắt đầu cập nhật Git... >> update_log.txt
cd /d d:\Downloads\Investments_WS2026
git add .
git commit -m "Auto-save local changes before daily update" >> update_log.txt 2>&1
git fetch upstream >> update_log.txt 2>&1
git merge upstream/main -m "Auto-merge daily upstream updates" >> update_log.txt 2>&1
echo [%date% %time%] Hoàn tất cập nhật. >> update_log.txt
echo ---------------------------------------- >> update_log.txt
