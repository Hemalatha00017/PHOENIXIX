from fastapi import APIRouter, UploadFile, File
from backend.voice_bot.service import process_audio

router = APIRouter()

@router.post("/call")
async def handle_call(audio: UploadFile = File(...)):
    result = await process_audio(audio)
    return {"status": "success", "data": result}
