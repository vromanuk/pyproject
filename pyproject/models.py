from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, Float, String

metadata = MetaData()

Contracts = Table(
    'contracts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(20), nullable=False, unique=True),
    Column('price', Float, nullable=False),
    Column('description', String(100), nullable=True)
)

Payments = Table(
    'payments',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('contracts_id', Integer, ForeignKey('contracts.id', onupdate='CASCADE', ondelete='CASCADE'),
           nullable=False),
    Column('amount', Float, nullable=False)
)
