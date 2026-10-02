"""
Flask application for the Docker CI/CD pipeline project.
Exposes a simple API with health check endpoint.
"""
import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Hello from Docker CI/CD pipeline",
        "hostname": socket.gethostname(),
        "version": os.getenv("APP_VERSION", "1.0.0")
    })


@app.route("/health")
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)