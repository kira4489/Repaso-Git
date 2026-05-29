from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hola Docker y Kubernetes"

app.run(host="0.0.0.0", port=5000)