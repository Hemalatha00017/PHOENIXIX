import os
from uuid import uuid4

TEMP_DIR = "temp_audio"
os.makedirs(TEMP_DIR, exist_ok=True)

def save_temp_audio(file):
    filename = f"{uuid4()}.wav"
    file_path = os.path.join(TEMP_DIR, filename)

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return file_path
