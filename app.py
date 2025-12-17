from flask import Flask, jsonify
import os
import logging

app = Flask(__name__)

# Config
APP_NAME = os.getenv("APP_NAME", "demo-flask-app")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

# Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

@app.route("/")
def index():
    app.logger.info("Root endpoint accessed")
    return jsonify({
        "service": APP_NAME,
        "version": APP_VERSION,
        "status": "running"
    })

@app.route("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/version")
def version():
    return jsonify({"version": APP_VERSION})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
