@echo off
echo ================================================
echo AI Guruji - Dependency Setup Script
echo ================================================
echo.

REM Activate virtual environment
echo [1/4] Activating virtual environment...
call venv\Scripts\activate.bat

REM Install Edge TTS (Microsoft - Much Faster!)
echo.
echo [2/4] Installing Edge TTS (Microsoft)...
pip install edge-tts==6.1.9

REM Add FFmpeg to current session PATH
echo.
echo [3/4] Setting up FFmpeg for current session...
set PATH=%CD%\tools\ffmpeg\bin;%PATH%
ffmpeg -version

REM Download Eunoic
echo.
echo [4/4] Downloading Eunoic avatar models...
cd backend
python download_eunoic.py
cd ..

echo.
echo ================================================
echo Setup Complete!
echo ================================================
echo.
echo Run 'python backend\check_deps.py' to verify.
pause
