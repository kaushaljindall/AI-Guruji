@echo off
echo Starting installation... > install.log
if exist "venv\Scripts\python.exe" (
    echo Found venv python. >> install.log
    "venv\Scripts\python.exe" setup_ffmpeg.py >> install.log 2>&1
) else (
    echo venv python not found, trying global python... >> install.log
    python setup_ffmpeg.py >> install.log 2>&1
)
echo Done. >> install.log
