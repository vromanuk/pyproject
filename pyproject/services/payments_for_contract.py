from sqlalchemy.sql import select
from pyproject.database import engine
from pyproject.models import Contracts, Payments


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
        query = select([Payments]).where(Contracts.c.id == contract_id).select_from(
            Contracts.outerjoin(Payments))
        result = conn.execute(query).fetchall()

        json_data = list()
        for i in result:
            json_data.append(dict(i))

        return json_data
