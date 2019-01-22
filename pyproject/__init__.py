from flask import Flask
from flask_restful import Api
from pyproject.logger import create_logger

app = Flask(__name__)
api = Api(app)
create_logger(app)

from pyproject import routes
