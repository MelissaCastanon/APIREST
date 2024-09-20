from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/saludo', methods=['GET'])
def saludo():
    # Crea un saludo
    mensaje = {
        'saludo': '¡Hola, bienvenido a la API!',
        'metodo': request.method
    }
    # Retorna el saludo en formato JSON
    return jsonify(mensaje)

if __name__ == '__main__':
    app.run(debug=True)
