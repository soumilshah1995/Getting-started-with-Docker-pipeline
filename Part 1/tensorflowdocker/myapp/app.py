
from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def hello():
    url = "http://myapp2:6000/"
    r = requests.get(url)
    return {
        "res":"m1",
        "ress":r.json()
    }

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)