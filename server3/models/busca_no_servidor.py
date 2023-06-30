import requests
from flask import request
from pymongo import MongoClient
from utils.serialize import custom_jsonify


def buscar_id_no_servidor(id, server):
    client = MongoClient(server['mongo_uri'])
    database = client[server['database']]
    collection = database["listingsAndReviews"]

    visited = request.args.get('visited')
    hasLocalID = collection.find_one({"_id": str(id)})

    if hasLocalID:
        return custom_jsonify(hasLocalID)

    visited_neighbors = [str(server['id'])] + (visited.split(',') if visited else [])
    neighbors = server["vizinhos"]

    for neighbor in neighbors:
        neighbor_id = str(neighbor["id"])

        if neighbor_id not in visited_neighbors:
            visited_neighbors.append(neighbor_id)
            visited_as_string = ','.join(visited_neighbors)
            response = None

            try:
                query = f"?visited={visited_as_string}" if visited_as_string else ''
                url = f"http://localhost:{neighbor['port']}/buscar/{id}{query}"
                response = requests.get(url).json()

            except:
                print(f"O servidor {neighbor_id} esta desligado ou inoperante."), 500

            if response and "_id" in response:
                return response

    return {"error": "ID nao encontrado em nenhum servidor"}, 404
