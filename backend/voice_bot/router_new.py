from fastapi import APIRouter, UploadFile, File, HTTPException
import os
import uuid
import librosa
import soundfile as sf
import noisereduce as nr
import whisper

router = APIRouter(prefix="/voice", tags=["Voice Bot"])

# Load model once at startup
MODEL = whisper.load_model("base")

@router.post("/upload")
async def upload_audio(file: UploadFile = File(...)):
    file_path = None
    clean_path = None
    
    try:
        # Save uploaded file
        file_path = f"backend/voice_bot/audio/{uuid.uuid4()}_{file.filename}"
        with open(file_path, "wb") as buffer:
            buffer.write(await file.read())
        
        # Preprocess audio
        y, sr = librosa.load(file_path, sr=16000)
        reduced_noise = nr.reduce_noise(y=y, sr=sr, prop_decrease=0.8, stationary=True)
        reduced_noise = librosa.util.normalize(reduced_noise)
        
        clean_path = f"backend/voice_bot/audio/clean_{uuid.uuid4()}.wav"
        sf.write(clean_path, reduced_noise, sr)
        
        # Transcribe
        audio_data, _ = librosa.load(clean_path, sr=16000)
        result = MODEL.transcribe(
            audio_data,
            language="en",
            fp16=False,
            temperature=0,
            beam_size=5,
            best_of=5
        )
        
        transcription = result.get("text", "").strip()
        
        if not transcription:
            raise ValueError("No speech detected")
        
        return {
            "status": "success",
            "transcription": transcription
        }
        
    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }
    
    finally:
        # Cleanup
        if file_path and os.path.exists(file_path):
            os.remove(file_path)
        if clean_path and os.path.exists(clean_path):
            os.remove(clean_path)
