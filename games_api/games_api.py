from flask import Flask, jsonify, abort, json
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(host='mongo')
db = client.gamesdb


@app.route('/games/<string:title>', methods=['GET'])
def games_by_title(title):
    query = {"title": title}
    projection = {"description": 1,
                  "game_id": 1,
                  "genres": 1,
                  "platforms": 1,
                  "moby_score": 1,
                  "title": 1,
                  "_id": 0}
    return jsonify([game for game in db.games.find(query, projection)])


@app.route('/genres', methods=['GET'])
def get_genres():
    return jsonify([genre for genre in db.genres.find(projection={"_id":0})])


@app.route('/consoles', methods=['GET'])
def get_consoles():
    return jsonify([console for console in db.platforms.find(projection={"_id":0})])


@app.route('/genres/<string:genre_name>', methods=['GET'])
def get_specific_genre(genre_name):
    query = {"genre_name": genre_name}
    projection = {"_id": 0}
    return jsonify([genre for genre in db.genres.find(query, projection)])


@app.route('/consoles/<string:console_name>', methods=['GET'])
def get_specific_console(console_name):
    query = {"platform_name": console_name}
    projection = {"_id": 0}
    return jsonify([platform for platform in db.platforms.find(query, projection)])

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
