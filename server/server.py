from flask import Flask

app = Flask(__name__)

@app.route('/')
def greeting():
    return "Hello World! Server is active"

if(__name__ == "__main__"):
    app.run(debug=True)