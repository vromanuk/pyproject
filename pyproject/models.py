from sqlalchemy import Table, MetaData, Column, ForeignKey, Integer, Float, String, Date
from datetime import date, datetime

metadata = MetaData()

Contracts = Table(
        'contracts',
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('title', String, nullable=False),
        Column('price', Float),
        Column('description', String),
        Column('expiration_date', Date, default=date.today())
        )

Payments = Table(
        'payments',
        metadata,
        Column('id', Integer, primary_key=True, autoincrement=True),
        Column('contracts_id', None, ForeignKey('contracts.id')),
        Column('amount', Float),
        Column('date_time', Date, default=datetime.now())
        )
