from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base=declarative_base()

class Atm(Base):
    __tablename__='atm'

    id=Column(INTEGER,primary_key=True)
    id_work_days_group=Column(INTEGER,ForeignKey('work_day_group.id'))
    id_bank=Column(INTEGER,ForeignKey('bank.id'))
    id_card_group=Column(INTEGER,ForeignKey('card_group.id'))
    id_action_group=Column(INTEGER,ForeignKey('action_group.id'))
    id_currency_group=Column(INTEGER,ForeignKey('currency_group.id'))
    lon=Column(FLOAT)
    lat=Column(FLOAT)
    address=Column(TEXT)
    update_date=Column(DATETIME)

class Action(Base):
    __tablename__='action'

    id=Column(INTEGER,primary_key=True)
    id_action_group=Column(INTEGER,ForeignKey('action_group.id'))
    value=Column(TEXT)


class Currency(Base):
    __tablename__='currency'

    id=Column(INTEGER,primary_key=True)
    id_currency_group=Column(INTEGER,ForeignKey('currency_group.id'))
    currency=Column(TEXT)

class Card(Base):
    __tablename__='card'

    id=Column(INTEGER,primary_key=True)
    id_card_group=Column(INTEGER,ForeignKey('card_group.id'))
    card=Column(TEXT)

class Card_group(Base):
    __tablename__='card_group'

    id=Column(INTEGER,primary_key=True)

    ref_atm=relationship('Atm',backref='card_group')
    ref_card=relationship('Card',backref='card_group')

class Action_group(Base):
    __tablename__='action_group'

    id=Column(INTEGER,primary_key=True)

    ref_atm=relationship('Atm',backref='action_group')
    ref_action=relationship('Action', backref='action_group')

class Currency_group(Base):
    __tablename__='currency_group'

    id=Column(INTEGER,primary_key=True)

    ref_atm=relationship('Atm',backref='currency_group')
    ref_curency=relationship('Currency', backref='currency_group')

class Work_days_group(Base):
    __tablename__='work_day_group'

    id=Column(INTEGER,primary_key=True)

    ref_atm=relationship('Atm',backref='work_day_group')
    ref_work_day=relationship('Work_day',backref='work_day_group')
    ref_work_day=relationship('Work_day',backref='work_day_group')

class Bank(Base):
    __tablename__='bank'

    id=Column(INTEGER,primary_key=True)

    name=Column(TEXT)
    contacts=Column(TEXT)
    site=Column(TEXT)

    ref_atm=relationship('Atm',backref='bank')

class Work_day(Base):
    __tablename__='work_day'

    id=Column(INTEGER,primary_key=True)

    id_work_days_group=Column(INTEGER,ForeignKey('work_day_group.id'))
    id_time=Column(INTEGER,ForeignKey('work_time.id'))
    week_day=Column(TEXT)

    ref_atm=relationship('Atm','work_day')


class Work_time(Base):
    __tablename__='work_time'

    id=Column(INTEGER,primary_key=True)

    start_time=Column(TIME)
    finish_time=Column(TIME)

    ref_work_day=relationship('Work_day', backref='work_time')
