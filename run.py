#!/usr/bin/env python3
"""
Simple launcher for vid2srt
"""
import sys
import os

# Add current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the main function
import argparse
import gui, splitter, transcriber

def main():
    parser = argparse.ArgumentParser(description="Vid2SRT: Video → Subtitles")
    parser.add_argument("--gui", action="store_true", help="Launch GUI mode")
    parser.add_argument("input", nargs="?", help="Input video file")
    parser.add_argument("--output-dir", default="./subs", help="Output directory")
    args = parser.parse_args()

    if args.gui:
        gui.launch()
    elif args.input:
        chunks = splitter.split_video(args.input)
        transcriber.transcribe_chunks(chunks, args.output_dir)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
