import os
import logging
from fastapi import FastAPI, HTTPException, Query
from starlette.responses import StreamingResponse
from smallest.async_tts import AsyncSmallest, APIError
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

# Load API key from environment variable
SMALLEST_API_KEY = os.getenv("SMALLEST_API_KEY")

# Ensure API key exists
if not SMALLEST_API_KEY:
    raise ValueError("Missing API key! Set 'SMALLEST_API_KEY' as an environment variable.")

# Initialize Smallest TTS client
tts = AsyncSmallest(api_key=SMALLEST_API_KEY)

# FastAPI App
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)


@app.post("/text-to-speech/")
async def text_to_speech(text: str = Query(..., min_length=1, description="Text to convert to speech")):
    """
    Converts text to speech using Smallest API and returns an audio stream.
    """
    try:
        audio_bytes = await tts.synthesize(text)

        # Convert binary data to a stream
        audio_stream = BytesIO(audio_bytes)

        # Return audio response with proper headers
        return StreamingResponse(
            audio_stream,
            media_type="audio/mpeg",
            headers={"Content-Disposition": "attachment; filename=output.mp3"}
        )

    except APIError as e:
        logging.error(f"TTS API Error: {e}")
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid or expired API key.")

    except Exception as e:
        logging.error(f"Unexpected Error: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error. Please try again later.")
