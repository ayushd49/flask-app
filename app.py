from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello from Docker on EC2!------re---------12</h1><p>Running inside a container on AWS.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)