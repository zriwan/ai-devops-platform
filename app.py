from flask import Flask, jsonify, render_template
import socket
import os
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "AI Powered DevOps Automation Platform",
        "status": "running",
        "server": socket.gethostname(),
        "environment": os.getenv("APP_ENV", "development"),
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/error")
def error():
    return jsonify({
        "status": "error",
        "message": "Sample error endpoint for monitoring test"
    }), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
