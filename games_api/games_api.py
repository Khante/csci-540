from flask import Flask, render_template, jsonify, abort, json
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(host='mongo')
db = client.gamesdb

@app.route('/games/<string:game_name>', methods = ['GET'])
def get_game(game_name):
	game = [game for game in db.games.find() if game['title'].replace(" ","") == game_name]
	if len(game)==0:
		abort(404)
	return jsonify({'description':game[0]['description'], 'platforms':game[0]['platforms'],'score':game[0]['moby_score'], 'title':game[0]['title'], '_id': str(game[0]['_id'])}) 

@app.route('/genre', methods = ['GET'])
def get_genre():
	genreList = []
	for genre in db.genres.find():
		name1 =  {'description':genre['genre_description'], 'category':genre['genre_category'], 'title':genre['genre_name'], 'genre_id': genre['genre_id']}
		genreList.append(name1)
	jsonStr =  json.dumps(genreList)
	return jsonify(Genres=jsonStr)
		
@app.route('/consoles', methods = ['GET'])
def get_console():
	consoleList = []
	for console in db.platforms.find():
		name1 =  {'platform_id':console['platform_id'], 'title':console['platform_name']}
		consoleList.append(name1)
	jsonStr =  json.dumps(consoleList)
	return jsonify(Consoles=jsonStr)

@app.route('/genre/<string:genre_name>', methods = ['GET'])
def get_specific_genre(genre_name):
	genre = [genre for genre in db.genres.find() if genre['genre_name'].replace(" ","") == genre_name]
	if len(genre)==0:
		abort(404)
	return jsonify({'description':genre[0]['genre_description'], 'category':genre[0]['genre_category'], 'title':genre[0]['genre_name'], 'genre_id': genre[0]['genre_id']}) 

@app.route('/consoles/<string:console_name>', methods = ['GET'])
def get_specific_console(console_name):
	console = [console for console in db.platforms.find() if console['platform_name'].replace(" ","") == console_name]
	if len(console)==0:
		abort(404)
	return jsonify({'platform_id':console[0]['platform_id'], 'title':console[0]['platform_name']}) 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
