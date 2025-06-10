from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def test():
    return "Hi"



app.run(host="0.0.0.0")