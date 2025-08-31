# Vid2SRT

A tool to convert video files to subtitle files (SRT format) using speech recognition.

## Features

- **Local Transcription**: Uses faster-whisper for offline speech recognition
- **GUI Interface**: User-friendly tkinter-based interface
- **CLI Support**: Command-line interface for automation
- **Video Splitting**: Automatically splits long videos into manageable chunks
- **Persistent Configuration**: Saves API keys and settings

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. **Install ffmpeg** (required for video processing):
   - **macOS**: `brew install ffmpeg` (requires Homebrew)
   - **Ubuntu/Debian**: `sudo apt install ffmpeg`
   - **Windows**: Download from https://ffmpeg.org/download.html

   **Note**: If you don't have Homebrew on macOS, install it first:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

   **Important**: FFmpeg is essential for video processing. The application will show a warning if FFmpeg is not found.

## Usage

### GUI Mode
```bash
python3 __main__.py --gui
# or
python3 run.py --gui
```

### CLI Mode
```bash
python3 __main__.py video.mp4 --output-dir ./subtitles
# or
python3 run.py video.mp4 --output-dir ./subtitles
```

## Project Structure

```
vid2srt/
├── __main__.py      # Entry point and CLI argument parsing
├── splitter.py      # Video splitting functionality
├── transcriber.py   # Speech recognition and transcription
├── gui.py          # GUI interface
├── utils.py        # Utility functions (SRT writing, cleanup)
├── config.py       # Configuration and API key management
└── __init__.py     # Package initialization
```

## How it Works

1. **Video Splitting**: Uses ffmpeg to split the video into 14-minute audio chunks
2. **Transcription**: Processes each chunk using faster-whisper
3. **SRT Generation**: Converts transcription results to SRT subtitle format
4. **Cleanup**: Removes temporary files after processing

## Configuration

API keys are stored in `~/.vid2srt_config.json` and persist between sessions.
