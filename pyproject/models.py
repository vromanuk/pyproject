from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, Float, String, Date
from datetime import date, datetime

metadata = MetaData()

Contracts = Table(
        'contracts',
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('title', String, nullable=False, unique=True),
        Column('price', Float, nullable=False),
        Column('description', String, nullable=True),
        Column('expiration_date', Date, default=date.today())
        )

Payments = Table(
        'payments',
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('contracts_id', Integer, ForeignKey('contracts.id')),
        Column('amount', Float, nullable=False),
        Column('date_time', Date, default=datetime.now())
        )
