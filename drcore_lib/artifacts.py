import os
import datetime

ARTIFACT_DIR = os.path.join(os.getcwd(), "artifacts")

def save_log(name, message):
    os.makedirs(ARTIFACT_DIR, exist_ok=True)
    filename = os.path.join(ARTIFACT_DIR, f"{name}.log")
    with open(filename, "a") as f:
        f.write(f"[{datetime.datetime.now().isoformat()}] {message}\n")
    return filename
