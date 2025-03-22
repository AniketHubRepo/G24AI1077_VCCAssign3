from flask import Flask, request, jsonify
from videototext import process_video
from database import insert_transcription

app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({"status": "UP"})

@app.route("/upload", methods=["POST"])
def upload_video():
    video = request.files["video"]
    video_path = f"./uploads/{video.filename}"
    video.save(video_path)
    text_output = process_video(video_path)
    insert_transcription(video.filename, text_output)
    return jsonify({"transcription": text_output})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)