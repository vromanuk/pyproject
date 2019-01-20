from sqlalchemy import create_engine
from pyproject.models import metadata, Contracts, Payments

engine = create_engine('postgres+psycopg2://postgres:postgres@localhost:5432/postgres', echo=True)


def create_all():
    metadata.create_all(engine)


def drop_all():
    metadata.drop_all(engine)


def populate():
    with engine.connect() as conn:
        conn.execute(Contracts.insert(), [
            {'title': 'HB1', 'price': 100.00,
             'description': 'Aspirin is used in the treatment of angina; heart attack'},
            {'title': 'E85', 'price': 78.25,
             'description': 'Penicillin V is an antibiotic in the penicillin group of drugs'}
        ])
    with engine.connect() as conn:
        conn.execute(Payments.insert(), [
            {'contracts_id': 1, 'amount': 15.00},
            {'contracts_id': 1, 'amount': 23.45},
            {'contracts_id': 2, 'amount': 22.00},
            {'contracts_id': 2, 'amount': 35.00}
        ])


if __name__ == '__main__':
    create_all()
    populate()

