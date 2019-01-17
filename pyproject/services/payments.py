from sqlalchemy.sql import select, update
from pyproject.database import engine
from pyproject.models import Payments


def get_payment_id(payment_id):
    """
    Retrieving payment's id
    :param payment_id: INT
    :return:
    """
    with engine.connect() as conn:
        query = select([Payments]).where(Payments.c.id == payment_id)
        result = conn.execute(query).first()

        return dict(result)


def add_new_payment(json_data):
    """
    Create a new payment
    :param json_data:
    :return:
    """
    with engine.connect() as conn:
        query = Payments.insert()
        conn.execute(query, json_data)

        return {'Message': 'Created successfully'}


def update_payment(json_data, payment_id):
    """
    Change payment
    :param json_data:
    :param payment_id:
    :return:
    """
    with engine.connect() as conn:
        query = update(Payments).where(Payments.c.id == payment_id).values(**json_data)
        conn.execute(query)
        payment = get_payment_id(payment_id)

        return dict(payment)


def delete_payment(payment_id):
    """
    Delete payment
    :param payment_id:
    :return:
    """
    with engine.connect() as conn:
        query = Payments.delete().where(Payments.c.id == payment_id)
        conn.execute(query)
        s = select([Payments]).where(Payments.c.id == payment_id).first()
        conn.execute(s)

        return dict(s)


def get_payments():
    """
    Retrieving all payments

    :return:
    """
    with engine.connect() as conn:
        query = select([Payments])
        result = conn.execute(query).fetchall()
        json_data = list()
        for i in result:
            json_data.append(dict(i))

        return json_data
