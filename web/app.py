import os
import socket

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! (HOSTNAME=%s, PID=%s)" % (socket.gethostname(), os.getpid())

if __name__ == "__main__":
    app.run()
