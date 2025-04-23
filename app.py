import os, json
from flask import Flask, request, jsonify

app = Flask(__name__)
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_emotion_data():
    data = request.json
    student_id = data.get("student", "unknown")
    records = data.get("records", [])

    filename = f"{DATA_DIR}/{student_id}_{int(time.time())}.json"
    with open(filename, "w") as f:
        json.dump(records, f)

    return jsonify({"status": "success", "message": f"Data saved for {student_id}."})

@app.route("/all", methods=["GET"])
def get_all_emotions():
    all_results = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".json"):
            with open(os.path.join(DATA_DIR, filename)) as f:
                try:
                    records = json.load(f)
                    all_results.extend(records)
                except:
                    continue
    return jsonify({"data": all_results})

@app.route("/")
def home():
    return "Student Emotion API is running!"
