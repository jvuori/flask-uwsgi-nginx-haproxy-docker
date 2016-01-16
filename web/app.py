import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! (PID=%s)" % (os.getpid())

if __name__ == "__main__":
    app.run()
