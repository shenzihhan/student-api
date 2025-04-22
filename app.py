from flask import Flask, request, jsonify
import os
import json
from datetime import datetime

app = Flask(__name__)
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_emotion():
    data = request.get_json()

    # 檔名格式：timestamp_studentname.json
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    name = data.get("student", "anonymous").replace(" ", "_")
    filename = f"{timestamp}_{name}.json"

    with open(os.path.join(DATA_DIR, filename), "w") as f:
        json.dump(data, f)

    return jsonify({"status": "success", "message": "Data saved."})

@app.route("/")
def home():
    return "Student Emotion API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
