@echo off
git diff --name-status | findstr "^M" > modified.txt
git diff --name-status | findstr "^D" > deleted.txt
git diff --name-status | findstr "^A" > added.txt
echo "Modified files saved to modified.txt"
echo "Deleted files saved to deleted.txt"
echo "Added files saved to added.txt"
pause