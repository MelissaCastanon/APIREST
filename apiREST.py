from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/saludo', methods=['GET', 'POST', 'PUT', 'DELETE'])
def saludo():
    if request.method == 'GET':
        mensaje = {
            'mensaje': '¡Hola, bienvenido a la API con método GET!'
        }
    elif request.method == 'POST':
        mensaje = {
            'mensaje': '¡Solicitud POST recibida! Se ha creado un nuevo recurso.'
        }
    elif request.method == 'PUT':
        mensaje = {
            'mensaje': '¡Solicitud PUT recibida! El recurso ha sido actualizado.'
        }
    elif request.method == 'DELETE':
        mensaje = {
            'mensaje': '¡Solicitud DELETE recibida! El recurso ha sido eliminado.'
        }

    return jsonify(mensaje)


if __name__ == '__main__':
    app.run(debug=True)
