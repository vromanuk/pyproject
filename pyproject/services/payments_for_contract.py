from sqlalchemy import text
from pyproject.database import engine
from pyproject.services.abstract_service import contract_


def get_payments_for_contract(contract_id: int):
    """
    Retrieve payments for the contract.

    :param contract_id: int
    :return:
    """
    if not contract_.is_resource_exist(contract_id):
        return {'Message': 'Such id does not exist'}
    with engine.connect() as conn:
        s = text("""
            SELECT contracts.title, contracts.price, contracts.description, payments.id, payments.amount
            FROM contracts 
            LEFT JOIN payments ON contracts.id = payments.contracts_id 
            WHERE contracts.id = :x""")
        query = s.bindparams(x=contract_id)
        result = conn.execute(query).fetchall()

        json_data = [dict(i) for i in result]

        return json_data
