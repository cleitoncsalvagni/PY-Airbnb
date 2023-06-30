from flask import Flask, jsonify, json

from models.busca_no_servidor import buscar_id_no_servidor

app = Flask(__name__)

with open('vizinhos2.json') as json_file:
    server = json.load(json_file)


@app.route("/buscar/", methods=["GET"])
def id_nao_fornecido():
    return jsonify({"error": "ID nao fornecido"}), 400


@app.route("/buscar/<int:id>", methods=["GET"])
def buscar_id_route(id):
    if not id:
        return json.dumps({"error": "ID nao fornecido"}), 400

    return buscar_id_no_servidor(id, server)


if __name__ == "__main__":
    app.run(port=5002)
