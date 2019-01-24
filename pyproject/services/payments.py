from sqlalchemy.sql import select, update
from pyproject.database import engine
from pyproject.models import Payments


def is_payment_exist(id_: int) -> bool:
    with engine.connect() as conn:
        query = select([Payments]).where(Payments.c.id == id_)
        result = conn.execute(query).first()

    return bool(result)


def get_payment_id(payment_id: int) -> dict:
    """
    Retrieve payment's id.

    :param payment_id: int
    :return: dict
    """
    if not is_payment_exist(payment_id):
        return {'Message': 'Such id does not exist'}
    with engine.connect() as conn:
        query = select([Payments]).where(Payments.c.id == payment_id)
        result = conn.execute(query).first()

        return dict(result)


def add_new_payment(json_data: dict) -> dict:
    """
    Create a new payment.

    :param json_data:
    :return: dict
    """
    with engine.connect() as conn:
        query = Payments.insert()
        conn.execute(query, json_data)

        return {'Message': 'Created successfully'}


def update_payment(json_data: dict, payment_id: int) -> dict:
    """
    Update an existing payment.

    :param json_data: dict
    :param payment_id: int
    :return: dict
    """
    if not is_payment_exist(payment_id):
        return {'Message': 'Such id does not exist'}
    with engine.connect() as conn:
        query = update(Payments).where(Payments.c.id == payment_id).values(**json_data)
        conn.execute(query)
        payment = get_payment_id(payment_id)

        return dict(payment)


def delete_payment(payment_id: int) -> dict:
    """
    Delete payment.

    :param payment_id: int
    :return: dict
    """
    if not is_payment_exist(payment_id):
        return {'Message': 'Such id does not exist'}
    with engine.connect() as conn:
        query = Payments.delete().where(Payments.c.id == payment_id)
        conn.execute(query)

        return {'Message': f'Contract {payment_id} deleted successfully'}


def get_payments():
    """
    Retrieve all payments.

    :return:
    """
    with engine.connect() as conn:
        query = select([Payments])
        result = conn.execute(query).fetchall()
        json_data = list()
        for i in result:
            json_data.append(dict(i))

        return json_data
