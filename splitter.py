import os
import subprocess
import tempfile
import shutil

# Video processing utilities for chunking large video files

def check_ffmpeg():
    return shutil.which("ffmpeg") is not None

def split_video(video_path, chunk_minutes=14):
    # Check if ffmpeg is available
    if not check_ffmpeg():
        raise RuntimeError(
            "ffmpeg is not installed or not found in PATH. "
            "Please install ffmpeg:\n"
            "  macOS: brew install ffmpeg\n"
            "  Ubuntu/Debian: sudo apt install ffmpeg\n"
            "  Windows: Download from https://ffmpeg.org/download.html"
        )
    
    temp_dir = tempfile.mkdtemp(prefix="vid2srt_")
    chunk_template = os.path.join(temp_dir, "chunk_%04d.wav")

    cmd = [
        "ffmpeg", "-i", video_path,
        "-f", "segment", "-segment_time", str(chunk_minutes * 60),
        "-c:a", "pcm_s16le", "-ar", "16000", chunk_template
    ]
    subprocess.run(cmd, check=True)

    return [os.path.join(temp_dir, f) for f in sorted(os.listdir(temp_dir))]
