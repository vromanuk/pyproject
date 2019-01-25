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
             'description': 'Penicillin V is an antibiotic in the penicillin group of drugs'},
            {'title': 'PGN', 'price': 28.88,
             'description': 'Lyrica is used to treat pain caused by nerve damage due to diabetes or spinal cord injury'},
            {'title': 'CIBA', 'price': 106.26,
             'description': 'Ritalin is used to treat attention deficit hyperactivity disorder'},
            {'title': '1S', 'price': 24.37,
             'description': 'Inositol is a vitamin-like substance. Used for diabetes, nerve problems.'}
        ])
    with engine.connect() as conn:
        conn.execute(Payments.insert(), [
            {'contracts_id': 1, 'amount': 15},
            {'contracts_id': 1, 'amount': 23},
            {'contracts_id': 2, 'amount': 22},
            {'contracts_id': 2, 'amount': 50},
            {'contracts_id': 3, 'amount': 10},
            {'contracts_id': 3, 'amount': 10},
            {'contracts_id': 3, 'amount': 40},
            {'contracts_id': 4, 'amount': 25},
            {'contracts_id': 4, 'amount': 100},
            {'contracts_id': 4, 'amount': 130},
            {'contracts_id': 5, 'amount': 3},
            {'contracts_id': 5, 'amount': 10}
        ])


if __name__ == '__main__':
    drop_all()
    create_all()
    populate()
