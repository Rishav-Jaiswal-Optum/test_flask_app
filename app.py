from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Hello Azure!"

@app.route("/test")
def test():
    return "Test Route"

if __name__ == "__main__":
    app.run()