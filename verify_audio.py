
import os
import sys

# Ensure current dir is in path to pick up pydub if installed locally? No, rely on venv.
# If pydub isn't installed, this will fail immediately.

# CRITICAL: Add local FFmpeg to PATH for this script execution
project_root = os.path.dirname(os.path.abspath(__file__))
ffmpeg_bin = os.path.join(project_root, "tools", "ffmpeg", "bin")
if os.path.exists(ffmpeg_bin):
    os.environ["PATH"] += os.pathsep + ffmpeg_bin
    print(f"Temporarily added local FFmpeg to PATH for verification: {ffmpeg_bin}")

print("Testing FFmpeg integration with pydub...")

try:
    import pydub
    from pydub import AudioSegment
    print(f"pydub version: {pydub.__version__}")
except ImportError:
    print("ERROR: pydub library not found.")
    print("Please run: pip install pydub")
    sys.exit(1)

try:
    # Create silent audio (1 second)
    print("Generating silent audio segment...")
    silence = AudioSegment.silent(duration=1000) 
    
    # Export it (requires ffmpeg)
    output_file = "test_audio.mp3"
    print(f"Attempting to export to {output_file}...")
    
    silence.export(output_file, format="mp3")
    
    if os.path.exists(output_file):
        print(f"SUCCESS: Exported {output_file}.")
        print("FFmpeg is correctly configured and accessible by pydub.")
        os.remove(output_file)
    else:
        print("FAILURE: Export failed (file not created).")

except FileNotFoundError:
    print("FAILURE: FFmpeg/FFprobe not found in PATH.")
    print("Please ensure 'ffmpeg' and 'ffprobe' commands work in your terminal.")
except Exception as e:
    print(f"FAILURE: An error occurred: {e}")
