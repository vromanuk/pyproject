import os
from logging import Formatter
from logging.handlers import RotatingFileHandler


def make_logger(app):
    """
    Creates logger handler for an application.

    :param app: Application
    """

    if not os.path.exists('logs/'):
        os.makedirs('logs/')

    file_handler = RotatingFileHandler('logs/Development.log', maxBytes=1000000, backupCount=1)
    file_handler.setLevel('DEBUG')
    file_handler.setFormatter(Formatter('%(asctime)s - %(levelname)s: %(message)s'))
    app.logger.addHandler(file_handler)
