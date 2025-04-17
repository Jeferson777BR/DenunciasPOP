from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

@app.route('/api/denuncia', methods=['POST'])
def receber_denuncia():
    data = request.get_json()
    conn = sqlite3.connect('backend/denuncias.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO denuncias (denunciado, descricao) VALUES (?, ?)", (data['denunciado'], data['descricao']))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 200

@app.route('/api/denuncias', methods=['GET'])
def listar_denuncias():
    conn = sqlite3.connect('backend/denuncias.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, denunciado, descricao, data_envio FROM denuncias ORDER BY data_envio DESC")
    denuncias = cursor.fetchall()
    conn.close()
    return jsonify(denuncias)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
