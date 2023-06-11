import whisper

model = whisper.load_model("base")
result = model.transcribe("common_voice_en_537.mp3")

with open("transcription.txt", "w") as f:
    f.write(result["text"])