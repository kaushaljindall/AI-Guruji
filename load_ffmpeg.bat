@echo off
set "PROJECT_ROOT=%~dp0"
set "FFMPEG_BIN=%PROJECT_ROOT%tools\ffmpeg\bin"

if exist "%FFMPEG_BIN%\ffmpeg.exe" (
    set "PATH=%FFMPEG_BIN%;%PATH%"
    echo [SUCCESS] FFmpeg added to current session PATH.
    echo Location: %FFMPEG_BIN%
    ffmpeg -version | findstr "version"
) else (
    echo [ERROR] FFmpeg binary not found at: %FFMPEG_BIN%
    echo Please run 'python setup_ffmpeg.py' first.
)
