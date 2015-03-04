from flask import Flask, render_template, request, jsonify
import dogo
import traceback

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/_summary', methods=["GET"])
def summary():
    try:
        song = request.args.get('a')    
        return jsonify(result=dogo.parse_it_asap(song))
    except Exception:
        return traceback.format_exc()

if __name__ == "__main__":
    app.run(debug = True)