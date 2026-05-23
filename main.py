from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def home():
    return "Success"


@app.route("/terminate")
def term():
    print("Ask for API Stoppage")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)