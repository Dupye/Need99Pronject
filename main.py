# app.py
import os
os.system('pip install flask')
from flask import Flask, request, jsonify

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
    app.run(debug=True)
    
