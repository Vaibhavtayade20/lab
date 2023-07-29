from flask import Flask, render_template

# create flask app
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/version", methods=["GET"])
def root():
    return "welcome to python flask app version1"


@app.route("/name", methods=["GET"])
def name():
    return "Vaibhav Tayade"

# run the application
app.run(host="0.0.0.0", port=4000, debug=True)

