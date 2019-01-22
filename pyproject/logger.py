import os
from logging import Formatter, FileHandler, DEBUG


def create_logger(app):
    """
    Creates logger handler for an application.

    :param app: Application
    """

    if not os.path.exists('logs/'):
        os.makedirs('logs/')

    app.logger.setLevel(DEBUG)
    formatter = Formatter('%(asctime)s - %(levelname)s: %(message)s')

    file_handler = FileHandler('logs/Development.log')
    file_handler.setFormatter(formatter)
    app.logger.addHandler(file_handler)

    return app
