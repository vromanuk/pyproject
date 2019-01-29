from pyproject import app
from flask import request
from flask_restful import Resource


class Smoke(Resource):

    def get(self):
        return 'OK', 200


@app.before_request
def wrapper():
    app.logger.info(f'{request.scheme} {request.remote_addr} {request.method} {request.path}')
