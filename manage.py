import argparse
import sys

from pyproject import app
from pyproject.database import create_all, drop_all, populate


def runserver(host, port):
    app.run(host=host, port=port, debug=True)


def db_init():
    drop_all()
    create_all()
    populate()


def parse_args(*args):
    parser = argparse.ArgumentParser(description="This is Flask app")
    subparser = parser.add_subparsers(dest="command")

    run = subparser.add_parser(runserver.__name__, add_help=False)
    run.add_argument("-h", "--host", dest="host", default="0.0.0.0", type=str)
    run.add_argument("-p", "--port", dest="port", default="5000", type=str)

    db_parse = subparser.add_parser(db_init.__name__, add_help=False)
    db_parse.add_argument(action="store_true", dest="db_init")
    return parser.parse_args(*args)


def main(args=None):
    args = parse_args(args or sys.argv[1:])
    print(args)
    if args.command == "runserver":
        runserver(args.host, args.port)
    elif args.command == "db_init":
        db_init()


if __name__ == '__main__':
    main()
