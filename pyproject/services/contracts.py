from sqlalchemy.sql import select, update

from pyproject.database import engine
from pyproject.models import Contracts
from flask import make_response


def get_contract_id(contract_id):
    """
    Retrieving contract's id
    :param contract_id: INT
    :return:
    """
    with engine.connect() as conn:
        query = select([Contracts]).where(Contracts.c.id == contract_id)
        result = conn.execute(query).first()
        d = dict(result)

        return d


def put_contract(json_data, contract_id):
    """
    Change contract
    :param json_data:
    :param contract_id:
    :return:
    """
    with engine.connect() as conn:
        query = update(Contracts).where(Contracts.c.id == contract_id).values(**json_data)
        conn.execute(query)
        contract = get_contract_id(contract_id)

        return contract


def delete_contract(contract_id):
    """
    Delete contract
    :param contract_id:
    :return:
    """
    with engine.connect() as conn:
        query = Contracts.delete().where(Contracts.c.id == contract_id)
        conn.execute(query)

        return {'Message': 'Deleted successfully'}, 200


def get_contracts():
    """
    Retrieving all contracts

    :return:
    """
    with engine.connect() as conn:
        query = select([Contracts])
        result = conn.execute(query).fetchall()
        l = list()
        for i in result:
            l.append(dict(i))

        return l


def add_new_contract(json_data):
    """
    Create a new contract
    :param json_data:
    :return:
    """
    with engine.connect() as conn:
        query = Contracts.insert()
        conn.execute(query, json_data)

        return {'Message': 'Created successfully'}, 201
