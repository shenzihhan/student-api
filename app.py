from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_emotion():
    data = request.get_json()

    # 這裡可以選擇進一步分析統計或即時儀表板展示用（目前直接回傳）
    student = data.get("student_id", "unknown")
    emotions = data.get("emotions", {})

    print(f"Received from {student}: {emotions}")

    return jsonify({
        "status": "success",
        "message": f"Received emotion data from {student}.",
        "emotions": emotions
    })

@app.route("/")
def home():
    return "Student Emotion API is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
