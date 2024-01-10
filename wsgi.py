from flask import Flask, render_template

from preds import main as preds_main

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/predict')
def predict():
    return preds_main()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
