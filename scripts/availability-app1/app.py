from flask import Flask, jsonify
from database import get_logs, init_db

app = Flask(__name__)

@app.route("/")
def home():
    return "Uptime Monitor Running"

@app.route("/logs")
def logs():
    return jsonify(get_logs())

@app.route("/uptime")
def uptime():
    logs = get_logs()
    total = len(logs)
    up = sum(1 for log in logs if log[2] == "UP")

    if total == 0:
        return {"uptime": 0}

    return {"uptime": round((up / total) * 100, 2)}

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)