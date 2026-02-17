@echo off
echo ================================================
echo   AI Guruji Frontend Server
echo ================================================
echo.

REM Navigate to frontend directory
cd /d "%~dp0\frontend"

echo [1/2] Installing dependencies (if needed)...
call npm install

echo [2/2] Starting frontend dev server...
echo.
echo Frontend running at: http://localhost:5173
echo.
echo Press Ctrl+C to stop the server
echo ================================================
echo.

npm run dev
