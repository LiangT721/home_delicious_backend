from flask import Flask, request, Response,render_template
import mariadb
import json
import random
from datetime import datetime
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/api/upload', methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, '/var/www/****/dist/img')   
    if not os.path.isdir(target):
        os.mkdir(target)
    files = request.files.getlist("file")
    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        destination = "/".join([target, filename])
        print(destination)
        file.save(destination)
    return Response(json.dumps(destination, default=str), mimetype="application/json", status=204)
if __name__=="__main__":
    app.run(port=4555,debug=True)