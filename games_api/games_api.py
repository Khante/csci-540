from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(host='mongo')


@app.route('/')
def games():

    db = client.gamesdb
    _consoles = db.platforms.find()
    consoles = [console for console in _consoles]

    return render_template('consoles.html', consoles=consoles)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
