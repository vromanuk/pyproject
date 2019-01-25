from sqlalchemy.sql import select, update
from pyproject.database import engine
from pyproject.models import Contracts


def is_contract_exist(id_: int) -> bool:
    with engine.connect() as conn:
        query = select([Contracts]).where(Contracts.c.id == id_)
        result = conn.execute(query).first()

    return bool(result)


def get_contract_id(contract_id: int) -> dict:
    """
    Retrieve contract's id.

    :param contract_id: int
    :return: dict
    """
    if not is_contract_exist(contract_id):
        return {'Message': 'Such id does not exist'}
    with engine.connect() as conn:
        query = select([Contracts]).where(Contracts.c.id == contract_id)
        result = conn.execute(query).first()

        return dict(result)


def add_new_contract(json_data: dict) -> dict:
    """
    Create a new contract.

    :param json_data: dict
    :return: dict
    """
    with engine.connect() as conn:
        query = Contracts.insert()
        conn.execute(query, json_data)

        return {'Message': 'Created successfully'}


def update_contract(json_data: dict, contract_id: int) -> dict:
    """
    Update an existing contract.

    :param json_data: dict
    :param contract_id: int
    :return: dict
    """
    if not is_contract_exist(contract_id):
        return {'Message': 'Such id does not exist'}
    with engine.connect() as conn:
        query = update(Contracts).where(Contracts.c.id == contract_id).values(**json_data)
        conn.execute(query)
        contract = get_contract_id(contract_id)

        return dict(contract)


def delete_contract(contract_id: int) -> dict:
    """
    Delete contract.

    :param contract_id: int
    :return: dict
    """
    if not is_contract_exist(contract_id):
        return {'Message': 'Such id does not exist'}
    with engine.connect() as conn:
        query = Contracts.delete().where(Contracts.c.id == contract_id)
        conn.execute(query)

        return {'Message': f'Contract {contract_id} deleted successfully'}


def get_contracts():
    """
    Retrieve all contracts.

    :return:
    """
    with engine.connect() as conn:
        query = select([Contracts])
        result = conn.execute(query).fetchall()
        json_data = [dict(i) for i in result]

        return json_data
