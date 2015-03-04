from flask import Flask, render_template, request, jsonify
import dogo
import sys
import logging

app = Flask(__name__)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/_summary', methods=["GET"])
def summary():
    try:
        song = request.args.get('a')    
        return jsonify(result=dogo.parse_it_asap(song))

if __name__ == "__main__":
    app.run(debug = True)