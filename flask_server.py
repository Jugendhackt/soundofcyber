from flask import Flask
from flask import jsonify
import os
import pathlib

import get_sound_data as GSD


app = Flask(__name__)

@app.route("/")
def index():
    # Bekomme den Pfad der Index-HTML Seite: Ist im gleichen Ordner, also selber Pfad
    html_path = pathlib.Path(__file__).parent.absolute() / "index.html"
    website = open(html_path, "r").read()
    # Webseite als Index anzeigen
    return website

@app.route("/get_sound_data")
def get_sound_data():
    data = GSD.get_sound_data()
    data = convert_to_json(data)
    return data

def convert_to_json(data):
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=1337, debug=True)