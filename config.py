import os
import json

CONFIG_PATH = os.path.expanduser("~/.vid2srt_config.json")

def save_key(key):
    data = {"api_key": key}
    with open(CONFIG_PATH, "w") as f:
        json.dump(data, f)

def load_key():
    if os.path.exists(CONFIG_PATH):
        try:
            with open(CONFIG_PATH) as f:
                return json.load(f).get("api_key")
        except Exception:
            return None
    return None
