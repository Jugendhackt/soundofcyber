from flask import Flask
import os
import pathlib

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
    

if __name__ == "__main__":
    app.run(port=1337, debug=True)