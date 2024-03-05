@echo off
git diff --name-status | findstr "^M" > modified.txt
git diff --name-status | findstr "^D" > deleted.txt
echo "Modified files saved to modified.txt"
echo "Deleted files saved to deleted.txt"
pause