@echo off
echo ================================================
echo   AI Guruji Backend Server
echo ================================================
echo.

REM Navigate to project root
cd /d "%~dp0"

REM Activate virtual environment (from project root)
echo [1/3] Activating virtual environment...
call venv\Scripts\activate.bat

REM Add FFmpeg to PATH for current session
echo [2/3] Setting up FFmpeg...
set PATH=%CD%\tools\ffmpeg\bin;%PATH%

REM Navigate to backend and start server
echo [3/3] Starting backend server...
cd backend
echo.
echo Backend running at: http://localhost:8000
echo API Docs at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo ================================================
echo.

uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
