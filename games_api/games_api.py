# import os
from flask import Flask, render_template
# from pymongo import MongoClient

app = Flask(__name__)

# client = MongoClient(
#     os.environ['DB_PORT_27017_TCP_ADDR'],
#     27017)
# db = client.gamesdb


@app.route('/')
def games():

    # _consoles = db.consoles.find()
    _consoles = [{"name": "PS2"}, {"name": "Nintendo64"}, {"name": "Xbox"}]
    consoles = [console for console in _consoles]

    return render_template('consoles.html', consoles=consoles)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
