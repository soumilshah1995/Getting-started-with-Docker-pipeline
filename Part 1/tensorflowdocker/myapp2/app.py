
from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    print("HERE")
    return {
        "res":"m2"
    }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=6000)