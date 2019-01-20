from flask import request
from flask_restful import Resource
from pyproject import app


class Smoke(Resource):
    def get(self):
        """
        Simple test that route exists.
        """
        app.logger.info(f'{request.scheme} {request.remote_addr} {request.method} {request.path}'
                        f'Requested Smoke Page')

        return {'message': 'OK'}, 200
