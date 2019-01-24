from flask import make_response
from marshmallow import ValidationError

from pyproject import app


@app.errorhandler(ValidationError)
def validation_error(error):
    app.logger.info(f'{error.message} {error.status_code}')
    return make_response({'Message': error.message}, error.status_code)


@app.error_handler(404)
def not_found_error(error):
    app.logger.info(f'{error.message} {error.status_code}')
    return make_response({'Message': error.message}, error.status_code)


@app.error_handler(500)
def internal_server_error(error):
    app.logger.info(f'{error.message} {error.status_code}')
    return make_response({'Message': error.message}, error.status_code)


@app.erorr_handler(ValueError)
def value_error(error):
    app.logger.info(f'{error.message} {error.status_code}')
    return make_response({'Message': error.message}, error.status_code)
