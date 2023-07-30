from flask import Flask, render_template

# create flask app
app = Flask(__name__)


#@app.route('/')
#def index():
#    return render_template('index.html')

@app.route("/", methods=["GET"])
def root():
    return "Welcome to the CICD Web"


@app.route("/me", methods=["GET"])
def name():
    return "PRN= 230344223053, Name: Vaibhav Tayade, Phone: 8208264088"

@app.route("/module", methods=["GET"])
def index():
    return render_template('index.html')

# run the application
app.run(host="0.0.0.0", port=4000, debug=True)

