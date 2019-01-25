from sqlalchemy import text
from sqlalchemy.sql import select
from pyproject.database import engine
from pyproject.models import Contracts


def is_contract_exist(id_: int) -> bool:
    with engine.connect() as conn:
        query = select([Contracts]).where(Contracts.c.id == id_)
        result = conn.execute(query).first()

    return bool(result)


def get_payments_for_contract(contract_id: int):
    """
    Retrieve payments for the contract.

    :param contract_id: int
    :return:
    """
    if not is_contract_exist(contract_id):
        return {'Message': 'Such id does not exist'}

    with engine.connect() as conn:
        s = text("""
            SELECT payments.amount, payments.id, contracts.title, contracts.price, contracts.description 
            FROM payments 
            LEFT JOIN contracts ON payments.contracts_id = contracts.id
            WHERE contracts_id = :x
            """)
        query = s.bindparams(x=contract_id)
        result = conn.execute(query).fetchall()

        json_data = list()
        for i in result:
            json_data.append(dict(i))

        return json_data
