from flask import Flask
from flask import jsonify
import os
import pathlib

import get_sound_data_example as GSD
import backend.DataAnalysis as DA


app = Flask(__name__)


directory_path = pathlib.Path(__file__).parent.absolute()

@app.route("/")
def index():
    # Bekomme den Pfad der Index-HTML Seite: Ist im gleichen Ordner, also selber Pfad
    html_path = directory_path / "index.html"
    website = open(html_path, "r").read()
    # Webseite als Index anzeigen
    return website

@app.route("/get_sound_data")
def get_sound_data():
    data = DA.Interpret()
    data = convert_to_json(data)
    return data

@app.route("/logo_dark_bg.svg")
def logodark():
    return open(directory_path / "logo_dark_bg.svg", encoding = "utf8").read(), 200, {'Content-Type': 'image/svg+xml charset=utf-8'}

@app.route("/logo.svg")
def logo():
    return open(directory_path / "logo.svg", encoding = "utf8").read(), 200, {'Content-Type': 'image/svg+xml charset=utf-8'}

def convert_to_json(data):
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=1337, debug=True)