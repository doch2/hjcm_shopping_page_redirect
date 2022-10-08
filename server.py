from flask import Flask, redirect
from flask_cors import CORS
import subprocess

url1 = "https://s.tosspayments.com/Bg7nVXz0K97"
url2 = "https://hjcmhjcm.cafe24.com/surl/O/21"

app = Flask(__name__)
CORS(app)

countVar = 0

@app.route("/")
def hello():
    global countVar

    if countVar % 2 == 0:
        connectUrl = url1
    else:
        connectUrl = url2

    countVar = countVar + 1
    

    return redirect(connectUrl)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)