# app.py
from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Rota /verify_udid
@app.route('/verify_udid', methods=['POST'])
def verify_udid():
    return jsonify({
        "status": "success",
        "message": "UDID verificado com sucesso!"
    })

# Rota /active_udid
@app.route('/active_udid', methods=['POST'])
def active_udid():
    return jsonify({
        "status": "success",
        "message": "UDID ativado com sucesso!"
    })

if __name__ == "__main__":
    # Render define a porta via variável de ambiente PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
