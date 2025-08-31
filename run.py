#!/usr/bin/env python3
"""
Simple launcher for vid2srt
Provides an alternative entry point for the application
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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
