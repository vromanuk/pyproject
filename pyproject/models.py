from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, Float, String

metadata = MetaData()

Contracts = Table(
        'contracts',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('title', String, nullable=False, unique=True),
        Column('price', Float, nullable=False),
        Column('description', String, nullable=True)
        )

Payments = Table(
        'payments',
        metadata,
        Column('id', Integer, primary_key=True),
        Column('contracts_id', Integer, ForeignKey('contracts.id')),
        Column('amount', Float, nullable=False)
        )
