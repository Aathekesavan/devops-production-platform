from flask import Flask, jsonify
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "🚀 DevOps Production App Running!"

@app.route("/health")
def health():
    return jsonify(status="healthy"), 200

@app.route("/slow")
def slow():
    time.sleep(2)
    return "Slow response (for testing)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)