from flask import Flask, render_template, request, jsonify
import dogo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/_summary')
def summary():
    song = request.args.get('a')
    summed = dogo.parse_it_asap(song)
    return jsonify(result=summed)

if __name__ == "__main__":
    app.run(debug = True)