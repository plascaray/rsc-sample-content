# -*- coding: utf-8 -*-
import os
import sys
from datetime import datetime

from flask import Flask
from flask_restx import Api, Resource, reqparse, fields

# Configure the Flask app using RestX for swagger documentation
app = Flask(__name__)
app.config["SWAGGER_UI_DOC_EXPANSION"] = "list"
app.config["RESTX_MASK_SWAGGER"] = False
app.config["ERROR_INCLUDE_MESSAGE"] = False

api = Api(
    app,
    version="0.1.0",
    title="Logs API",
    description="This rest API writes log statements to the underlying filesystem or to stdout/stderr",
)

ns = api.namespace("log")

parser = reqparse.RequestParser()
parser.add_argument("msg")

@ns.route("/stdout")
@api.doc(params={'msg': 'A log message'})
class Stdout(Resource):
    """Writes a string to stdout"""

    def post(self):
        args = parser.parse_args()
        now = datetime.now()
        msg = args['msg']
        sys.stdout.write(f"{now} - {msg}\n")
        sys.stdout.flush()
        return 200

@ns.route("/stderr")
@api.doc(params={'msg': 'A log message'})
class Stderr(Resource):
    """Writes a string to stderr"""

    def post(self):
        args = parser.parse_args()
        now = datetime.now()
        msg = args['msg']
        sys.stderr.write(f"{now} - {msg}\n")
        sys.stderr.flush()
        return 200

@ns.route("/file")
@api.doc(params={'msg': 'A log message'})
class File(Resource):
    """Writes a string to a file on the underlying filesystem"""

    def post(self):
        args = parser.parse_args()
        now = datetime.now()
        msg = args['msg']
        with open("log.txt", 'a') as f:
            f.write(f"{now} - {msg}\n")
            f.flush()
        return 200

if __name__ == "__main__":
    app.run(debug=True)
