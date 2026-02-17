
import os
import sys
import zipfile
import shutil
import urllib.request
import subprocess
import winreg
import ssl
from pathlib import Path

# Configuration
FFMPEG_URL = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
DOWNLOAD_PATH = "ffmpeg.zip"
# Install locally to avoid 'Access is denied' on C:\ or HKLM
INSTALL_DIR = os.path.join(os.getcwd(), "tools", "ffmpeg")

def download_ffmpeg():
    print(f"Downloading FFmpeg from {FFMPEG_URL}...")
    if os.path.exists(DOWNLOAD_PATH):
        if os.path.getsize(DOWNLOAD_PATH) > 1000000: # > 1MB
            print("Zip already exists and looks valid, skipping download.")
            return
        else:
            print("Existing zip is too small (likely corrupt), redownloading...")
            os.remove(DOWNLOAD_PATH)
        
    # Method 1: Python urllib with SSL bypass
    try:
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        
        with urllib.request.urlopen(FFMPEG_URL, context=ctx) as u, open(DOWNLOAD_PATH, 'wb') as f:
            meta = u.info()
            file_size = int(meta.get("Content-Length", 0))
            print(f"File size: {file_size / 1024 / 1024:.2f} MB")
            
            file_size_dl = 0
            block_sz = 8192
            while True:
                buffer = u.read(block_sz)
                if not buffer:
                    break
                
                file_size_dl += len(buffer)
                f.write(buffer)
                
                if file_size:
                    sys.stdout.write(f"\rDownloading... {file_size_dl * 100 / file_size:.2f}%")
                    sys.stdout.flush()

        print("\nDownload complete.")
        return
    except Exception as e:
        print(f"\nPython download failed: {e}")

    # Method 2: Curl fallback (Windows 10+ has curl)
    try:
        print("Trying fallback with curl...")
        # -k (insecure/skip ssl), -L (follow redirects), -o (output header)
        subprocess.run(["curl", "-k", "-L", "-o", DOWNLOAD_PATH, FFMPEG_URL], check=True)
        print("Curl download successful.")
    except Exception as e:
        print(f"Curl fallback failed: {e}")
        print("Please manually download the file from:")
        print(f"{FFMPEG_URL}")
        print(f"Save it as '{DOWNLOAD_PATH}' in this folder and run the script again.")
        sys.exit(1)

def extract_ffmpeg():
    print(f"Extracting to {INSTALL_DIR}...")
    
    # Clean previous install
    if os.path.exists(INSTALL_DIR):
        try:
            shutil.rmtree(INSTALL_DIR)
        except Exception as e:
            print(f"Warning: Could not clean target directory: {e}")

    # Extract
    try:
        with zipfile.ZipFile(DOWNLOAD_PATH, "r") as zip_ref:
            # Extract to temp dir first to find the inner folder
            extract_root = os.path.join(os.getcwd(), "tools", "temp_extract")
            if os.path.exists(extract_root):
                shutil.rmtree(extract_root)
            os.makedirs(extract_root, exist_ok=True)
            
            zip_ref.extractall(extract_root)
            
            # Find the internal folder (e.g. ffmpeg-6.0-full_build)
            extracted_items = os.listdir(extract_root)
            ffmpeg_root = None
            for item in extracted_items:
                if item.lower().startswith("ffmpeg"):
                    ffmpeg_root = os.path.join(extract_root, item)
                    break
            
            if not ffmpeg_root:
                print("Could not find ffmpeg folder in zip.")
                sys.exit(1)
                
            # Move to final location
            shutil.move(ffmpeg_root, INSTALL_DIR)
            
            # Cleanup temp
            shutil.rmtree(extract_root)
            
    except Exception as e:
        print(f"Extraction failed: {e}")
        sys.exit(1)

    print("Extraction complete.")

def add_to_path():
    print("Adding FFmpeg to User PATH...")
    
    ffmpeg_bin = os.path.join(INSTALL_DIR, "bin")
    if not os.path.exists(ffmpeg_bin):
        print(f"Error: Bin directory not found at {ffmpeg_bin}")
        return

    # User Environment Variable (HKCU) - No Admin required
    try:
        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Environment",
            0,
            winreg.KEY_READ | winreg.KEY_WRITE,
        )
        
        try:
            current_path, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            current_path = "" # Create if empty

        if ffmpeg_bin.lower() not in current_path.lower():
            # Append
            new_path = current_path
            if new_path and not new_path.endswith(";"):
                new_path += ";"
            new_path += ffmpeg_bin
            
            winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path)
            print(f"Success: Added {ffmpeg_bin} to User PATH.")
        else:
            print("FFmpeg is already in User PATH.")

        winreg.CloseKey(key)
        
        # Update current process path so verification works immediately
        os.environ["PATH"] += os.pathsep + ffmpeg_bin
        
    except Exception as e:
        print(f"Registry update failed: {e}")
        print("You may need to add it manually.")

def verify_installation():
    print("Verifying installation...")
    try:
        # Check specific binary first
        ffmpeg_exe = os.path.join(INSTALL_DIR, "bin", "ffmpeg.exe")
        if not os.path.exists(ffmpeg_exe):
            print(f"Error: ffmpeg.exe not found at {ffmpeg_exe}")
            return

        # Run it
        result = subprocess.run(
            [ffmpeg_exe, "-version"],
            capture_output=True,
            text=True,
            check=True,
        )
        print("FFmpeg verification successful!")
        print(result.stdout.split("\n")[0])
        
    except Exception as e:
        print(f"Verification failed: {e}")

def cleanup():
    if os.path.exists(DOWNLOAD_PATH):
        try:
            os.remove(DOWNLOAD_PATH)
            print("Cleanup done.")
        except:
            pass

def main():
    # Ensure tools dir exists
    os.makedirs(os.path.join(os.getcwd(), "tools"), exist_ok=True)

    download_ffmpeg()
    extract_ffmpeg()
    add_to_path()
    verify_installation()
    cleanup()
    
    print("\nIMPORTANT: You may need to restart your terminal/IDE for PATH changes to stick.")

if __name__ == "__main__":
    main()
