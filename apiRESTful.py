from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Base URL de la API Mock
MOCK_API_URL = "https://64f8f2604098a7f2fc13f7f8.mockapi.io/IoTCarStatus"

# Obtener todos los registros
@app.route('/status', methods=['GET'])
def get_all_status():
    response = requests.get(MOCK_API_URL)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Error al obtener los datos'}), response.status_code

# Obtener un registro por ID
@app.route('/status/<int:id>', methods=['GET'])
def get_status_by_id(id):
    response = requests.get(f"{MOCK_API_URL}/{id}")
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Registro no encontrado'}), response.status_code

# Crear un nuevo registro
@app.route('/status', methods=['POST'])
def create_status():
    new_status = request.json
    response = requests.post(MOCK_API_URL, json=new_status)
    if response.status_code == 201:
        return jsonify(response.json()), 201
    else:
        return jsonify({'error': 'Error al crear el registro'}), response.status_code

# Actualizar un registro existente por ID
@app.route('/status/<int:id>', methods=['PUT'])
def update_status(id):
    updated_status = request.json
    response = requests.put(f"{MOCK_API_URL}/{id}", json=updated_status)
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({'error': 'Error al actualizar el registro'}), response.status_code

# Eliminar un registro por ID
@app.route('/status/<int:id>', methods=['DELETE'])
def delete_status(id):
    response = requests.delete(f"{MOCK_API_URL}/{id}")
    if response.status_code == 200:
        return jsonify({'message': 'Registro eliminado'}), 200
    else:
        return jsonify({'error': 'Error al eliminar el registro'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
