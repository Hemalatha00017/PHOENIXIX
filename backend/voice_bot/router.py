from fastapi import APIRouter, UploadFile, File
from backend.voice_bot.service import process_audio

router = APIRouter(prefix="/voice", tags=["Voice Bot"])

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    text = await process_audio(file)
    return {
        "status": "success",
        "transcribed_text": text
    }
