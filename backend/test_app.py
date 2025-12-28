from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "FLASK IS RUNNING"

@app.route("/test")
def test():
    return "TEST ROUTE WORKS"

if __name__ == "__main__":
    app.run(debug=True)
