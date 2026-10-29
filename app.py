from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Workfront Engineer Learning Git and Azure 🚀"

@app.route("/test") 
def test():
    return "Test Route Modified 🚀"

if __name__ == "__main__":
    app.run()