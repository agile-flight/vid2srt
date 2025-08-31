import tkinter as tk
from tkinter import filedialog, ttk, messagebox
import splitter, transcriber, config
import threading
import os

# Graphical user interface for vid2srt application

def launch():
    root = tk.Tk()
    root.title("Vid2SRT")

    # Check if ffmpeg is available
    if not splitter.check_ffmpeg():
        messagebox.showwarning(
            "FFmpeg Not Found", 
            "FFmpeg is not installed or not found in PATH.\n\n"
            "Please install FFmpeg:\n"
            "• macOS: brew install ffmpeg\n"
            "• Ubuntu/Debian: sudo apt install ffmpeg\n"
            "• Windows: Download from https://ffmpeg.org/download.html\n\n"
            "The application will not work without FFmpeg."
        )

    file_var = tk.StringVar()
    out_var = tk.StringVar(value=os.getcwd())
    key_var = tk.StringVar(value=config.load_key() or "")

    def browse_file():
        path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4;*.mkv;*.mov")])
        if path:
            file_var.set(path)

    def browse_output():
        path = filedialog.askdirectory()
        if path:
            out_var.set(path)

    def start():
        video = file_var.get()
        output = out_var.get()
        key = key_var.get().strip()
        if key:
            config.save_key(key)
        if not video:
            messagebox.showerror("Error", "Please select a video file")
            return

        progress["value"] = 0
        btn_start.config(state=tk.DISABLED)

        def worker():
            try:
                chunks = splitter.split_video(video)
                total = len(chunks)

                for idx, chunk in enumerate(chunks):
                    transcriber.transcribe_chunks([chunk], output)
                    progress["value"] = ((idx+1)/total) * 100

                messagebox.showinfo("Done", f"Subtitles saved to {output}")
            except RuntimeError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {str(e)}")
            finally:
                btn_start.config(state=tk.NORMAL)

        threading.Thread(target=worker, daemon=True).start()

    tk.Label(root, text="Video:").grid(row=0, column=0, sticky="e")
    tk.Entry(root, textvariable=file_var, width=40).grid(row=0, column=1)
    tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2)

    tk.Label(root, text="Output:").grid(row=1, column=0, sticky="e")
    tk.Entry(root, textvariable=out_var, width=40).grid(row=1, column=1)
    tk.Button(root, text="Browse", command=browse_output).grid(row=1, column=2)

    tk.Label(root, text="API Key:").grid(row=2, column=0, sticky="e")
    tk.Entry(root, textvariable=key_var, width=40, show="*").grid(row=2, column=1)

    btn_start = tk.Button(root, text="Start", command=start)
    btn_start.grid(row=3, column=1, pady=10)

    progress = ttk.Progressbar(root, length=300, mode="determinate")
    progress.grid(row=4, column=0, columnspan=3, pady=5)

    root.mainloop()
