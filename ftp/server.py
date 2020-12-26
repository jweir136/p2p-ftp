import flask
import os

app = flask.Flask(__name__)

@app.route("/<filename>")
def index(filename):
    with open(os.path.join("ftp", "assets", filename), 'r') as f:
        return f.read()

if __name__ == "__main__":
    app.run(host="0.0.0.0")