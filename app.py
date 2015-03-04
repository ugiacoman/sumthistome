from flask import Flask, render_template, request, jsonify
from dogo import parse_it_asap

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/_summary')
def summary():
    song = request.args.get('a', 0, type=str)
    summed = dogo.parse_it_asap(song)
    return jsonify(result=summed)

if __name__ == "__main__":
    app.run(debug = True)