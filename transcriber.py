import os
from faster_whisper import WhisperModel
import utils, config

def transcribe_chunks(chunks, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    key = config.load_key()
    if key:
        print("Using OpenAI Whisper API (not implemented stub here)")
        # TODO: implement OpenAI API transcription if key provided
    else:
        print("Using local faster-whisper")
        model = WhisperModel("small", device="auto", compute_type="int8_float16")
        for idx, chunk in enumerate(chunks):
            segments, _ = model.transcribe(chunk)
            srt_path = os.path.join(output_dir, f"chunk_{idx+1:04d}.srt")
            utils.write_srt(segments, srt_path)
            print(f"Saved {srt_path}")

    utils.cleanup_temp(chunks)
