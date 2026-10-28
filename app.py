from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Workfront Engineer Learning Azure 🚀"

@app.route("/test")
def test():
    return "Test Route"

if __name__ == "__main__":
    app.run()