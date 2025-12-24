from fastapi import APIRouter, UploadFile, File
from backend.voice_bot.service import process_audio
import shutil

router = APIRouter(prefix="/voice")

@router.post("/analyze-call")
async def analyze_call(file: UploadFile = File(...)):
    file_path = f"temp_audio/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = process_audio(file_path)

    return result
