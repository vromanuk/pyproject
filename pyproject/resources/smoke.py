from flask_restful import Resource


class Smoke(Resource):
    def get(self):
        """
        Simple test that route exists.
        """
        return {'message': 'OK'}, 200

