from datetime import datetime, timezone
from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.now(timezone.utc).isoformat()})


@app.route("/items")
def items():
    return jsonify([
        {"id": 1, "name": "Item A"},
        {"id": 2, "name": "Item B"},
    ])


# Local development
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
