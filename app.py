
from flask import Flask, render_template, request
from dogo import parse_it_asap

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def my_form_post():
    song = request.form['text']
    summed = parse_it_asap(song)
    return summed

if __name__ == "__main__":
    app.run(debug = True)

