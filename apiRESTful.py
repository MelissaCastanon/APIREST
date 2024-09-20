from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# URL base de la API MockAPI
BASE_URL = 'https://66eb029a55ad32cda47b53b8.mockapi.io/IoTCarStatus'


# Obtener todos los recursos o uno específico por ID
@app.route('/resource', methods=['GET'])
def get_resource():
    resource_id = request.args.get('id')
    if resource_id:
        # Obtener un recurso específico
        response = requests.get(f'{BASE_URL}/{resource_id}')
    else:
        # Obtener todos los recursos
        response = requests.get(BASE_URL)

    if response.status_code == 404:
        return jsonify({"error": "Recurso no encontrado"}), 404
    return jsonify(response.json()), response.status_code


# Crear un nuevo recurso
@app.route('/resource', methods=['POST'])
def create_resource():
    data = {
        "Status": request.json.get('Status', "Active"),
        "Date": request.json.get('Date', "2024-09-19T12:00:00Z"),
        "ipClient": request.json.get('ipClient', "127.0.0.1"),
        "name": request.json.get('name', "John Doe")
    }
    response = requests.post(BASE_URL, json=data)
    return jsonify(response.json()), response.status_code


# Actualizar un recurso existente
@app.route('/resource', methods=['PUT'])
def update_resource():
    resource_id = request.args.get('id')
    if not resource_id:
        return jsonify({"error": "Debe proporcionar un ID para actualizar el recurso"}), 400

    data = request.json
    response = requests.put(f'{BASE_URL}/{resource_id}', json=data)

    if response.status_code == 404:
        return jsonify({"error": "Recurso no encontrado"}), 404

    return jsonify(response.json()), response.status_code


# Eliminar un recurso existente
@app.route('/resource', methods=['DELETE'])
def delete_resource():
    resource_id = request.args.get('id')
    if not resource_id:
        return jsonify({"error": "Debe proporcionar un ID para eliminar el recurso"}), 400

    response = requests.delete(f'{BASE_URL}/{resource_id}')

    if response.status_code == 404:
        return jsonify({"error": "Recurso no encontrado"}), 404

    return '', response.status_code


if __name__ == '__main__':
    app.run(debug=True)
