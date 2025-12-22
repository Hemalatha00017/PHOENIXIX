from fastapi import FastAPI
from backend.voice_bot.router import router as voice_router

app = FastAPI(title="Medical Voice Bot")

app.include_router(voice_router, prefix="/voice")
