from flask import Flask, request, jsonify
import requests
import os
import json

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1459885767114489989/GWXlATcxonVZw7rgZf6zZDeh1r6VnJF9E0RFlIqkXR1a3Sjs3p7PLg7v6Tpp3gLDqTJM"


def collect_request_data():
    return {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": request.get_json(silent=True),
        "raw": request.get_data(as_text=True)
    }


def send_to_discord(title, data):
    content = f"**{title}**\n```json\n{json.dumps(data, indent=2, ensure_ascii=False)}\n```"
    try:
        requests.post(WEBHOOK_URL, json={"content": content}, timeout=5)
    except Exception:
        pass


@app.route("/verify_udid", methods=["GET", "POST"])
def verify_udid():
    data = collect_request_data()
    send_to_discord("VERIFY_UDID", data)

    return jsonify({
        "status": "success",
        "valid": True,
        "active": True,
        "autowin": True
    }), 200


@app.route("/active_udid", methods=["GET", "POST"])
def active_udid():
    data = collect_request_data()
    send_to_discord("ACTIVE_UDID", data)

    return jsonify({
        "status": "success",
        "activated": True,
        "message": "Cracked by Dupp 🤪"
    }), 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
