import flask
import os
import sys

app = flask.Flask(__name__)

@app.route("/<filename>")
def index(filename):
    with open(os.path.join("assets", filename), 'r') as f:
        return f.read()

if __name__ == "__main__":
    host = sys.argv[1]
    app.run(host=str(host))