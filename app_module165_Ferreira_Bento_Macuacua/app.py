import os
from flask import Flask, render_template, request
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = os.getenv("MONGO_DB", "my_data_Ferreira_Bento_Macuacua")
COLLECTION_NAME = os.getenv("MONGO_COLLECTION", "open_data")

client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=3000)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]


def get_error_message():
    try:
        client.admin.command("ping")
        return None
    except ServerSelectionTimeoutError as error:
        return f"Connexion MongoDB impossible : {error}"


@app.route("/")
def index():
    error = get_error_message()
    pokemons = [] if error else list(collection.find().limit(50))
    return render_template("index.html", pokemons=pokemons, error=error)


@app.route("/search")
def search():
    error = get_error_message()
    name = request.args.get("name", "").strip()
    type_1 = request.args.get("type_1", "").strip()

    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if type_1:
        query["type_1"] = type_1

    pokemons = [] if error else list(collection.find(query).limit(100))
    return render_template("search.html", pokemons=pokemons, name=name, type_1=type_1, error=error)


@app.route("/stats")
def stats():
    error = get_error_message()
    top_pokemons = []
    types = []
    if not error:
        top_pokemons = list(collection.find().sort("base_stat_total", -1).limit(10))
        types = list(collection.aggregate([
            {"$group": {"_id": "$type_1", "total": {"$sum": 1}}},
            {"$sort": {"total": -1}}
        ]))
    return render_template("stats.html", top_pokemons=top_pokemons, types=types, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
