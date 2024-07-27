from TTS.api import TTS
from flask import Flask, request, send_file
from flask_cors import CORS
import io
import soundfile as sf

app = Flask(__name__)
CORS(app)

# Initialize TTS with the correct multi-speaker model
tts = TTS(model_name="tts_models/en/vctk/vits")  # Update this with the correct model name

@app.route("/api/tts", methods=["POST"])
def tts_route():
    text = request.json.get("text", "")
    speaker_id = request.json.get("speaker_id", None)

    print(f"Received request with text: {text}, speaker: {speaker_id}")
    
    # Generate speech
    wav = tts.tts(text=text, speaker=speaker_id)
    
    # Convert to WAV format
    wav_io = io.BytesIO()
    sf.write(wav_io, wav, samplerate=tts.synthesizer.output_sample_rate, format='WAV')
    wav_io.seek(0)
    
    return send_file(wav_io, mimetype="audio/wav")

@app.route("/api/speakers", methods=["GET"])
def get_speakers():
    return {"speakers": tts.speakers}

if __name__ == "__main__":
    app.run(port=5002, debug=True)