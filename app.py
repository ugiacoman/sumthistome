from flask import Flask, render_template, request, jsonify
import dogo

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/_summary', methods=["GET"])
def summary():
    song = request.args.get('a')
    return jsonify(result=dogo.parse_it_asap(song))

if __name__ == "__main__":
    app.run(debug = True)