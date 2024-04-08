from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_hbnb():
    return "<p>Hello HBNB!</p>"