import os
import socket
import time

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    time.sleep(0.1)
    return "Hello World! (HOSTNAME=%s, PID=%s)" % (socket.gethostname(), os.getpid())

if __name__ == "__main__":
    app.run()
