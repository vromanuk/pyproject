from flask import Flask
from flask_restful import Api
from pyproject.logger import make_logger

app = Flask(__name__)
api = Api(app)
make_logger(app)

from pyproject import routes
