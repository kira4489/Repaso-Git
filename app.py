from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Esto es un proyecto DevOps con Docker y Kubernettes"

app.run(host="0.0.0.0", port=5000)