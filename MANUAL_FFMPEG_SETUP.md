# Manual FFmpeg Setup Guide

FFmpeg is a critical dependency for audio and video processing in AI Guruji. If the automatic setup script failed, please follow these steps to install it manually.

## 1. Download FFmpeg
1. Visit the download page: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
2. Scroll down to the "release" section.
3. Download **ffmpeg-release-essentials.zip**.
   - Direct Link: [https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip](https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip)
   - **Alternative Link (GitHub)**: If the above fails, use [BtbN/FFmpeg-Builds](https://github.com/BtbN/FFmpeg-Builds/releases) and download `ffmpeg-master-latest-win64-gpl.zip`.

## 2. Extract Files
1. Create a folder named `tools` in the project root: `d:\Projects\AI-Guruji\tools`.
2. Extract the downloaded zip file content into this folder.
   - You should see a folder like `ffmpeg-6.0-essentials_build` (version may vary).
3. Rename the extracted folder to simply `ffmpeg` for easier access.
   - Structure should look like: `d:\Projects\AI-Guruji\tools\ffmpeg\bin\ffmpeg.exe`

## 3. Add to System PATH
To make FFmpeg accessible from any terminal:
1. Open **Start Menu** and search for "Edit the system environment variables".
2. Click **Environment Variables**.
3. Under **User variables** (top section), find `Path` and click **Edit**.
4. Click **New** and add the full path to the `bin` folder:
   ```
   d:\Projects\AI-Guruji\tools\ffmpeg\bin
   ```
5. Click **OK** on all dialogs.

## 4. Verify Installation
1. Open a **new** terminal window (or restart your IDE).
2. Run the following command:
   ```cmd
   ffmpeg -version
   ```
3. If successful, you will see version information (e.g., `ffmpeg version 6.0...`).

## Troubleshooting
- **"ffmpeg is not recognized..."**: Ensure you added the `bin` folder (containing `ffmpeg.exe`), not just the main folder.
- **Still failing?**: Try restarting your computer to refresh all environment variables.
