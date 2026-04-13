from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello, Flask90000!</h1><p>My first Flask app.</p>"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0', port=5000)
