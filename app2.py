@@ -1,11 +1,20 @@
# app.py
from flask import Flask
from flask import request

import requests
import re
import socket

app = Flask(__name__)

@app.route('/')
def hello_flask():
    return "Hello, Webapp!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
