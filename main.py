from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def log_request():
    print("=== NOVA REQUISIÇÃO ===")
    print("Método:", request.method)
    print("URL:", request.url)
    print("Headers:", dict(request.headers))
    print("Args (GET):", request.args.to_dict())
    print("Form:", request.form.to_dict())
    print("JSON:", request.get_json(silent=True))
    print("Raw data:", request.get_data(as_text=True))
    print("======================")

@app.route('/verify_udid', methods=['POST', 'GET'])
def verify_udid():
    log_request()
    return jsonify({
        "status": "success",
        "message": "UDID verificado com sucesso!"
    })

@app.route('/active_udid', methods=['POST', 'GET'])
def active_udid():
    log_request()
    return jsonify({
        "status": "success",
        "message": "UDID ativado com sucesso!"
    })

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
