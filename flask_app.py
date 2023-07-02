# site to be redirected to if port scanner finds the ip and port open

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Goodbye, World!"

if __name__ == "__main__":
    app.run()
