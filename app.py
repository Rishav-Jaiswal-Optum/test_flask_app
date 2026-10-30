from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return os.getenv("MESSAGE")

@app.route("/test") 
def test():
    return "Test Route Modified 🚀"

if __name__ == "__main__":
    app.run()