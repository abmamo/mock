# sqlalchemy declarative base
from sqlalchemy.ext.declarative import declarative_base
# sqlalchemy column types
from sqlalchemy import Column, Integer, String, DateTime
# init sqlalchemy declarative base
Base = declarative_base()


class Person(Base):
    __tablename__ = 'persons'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        self.name = name


class Currency(Base):
    __tablename__ = 'currencies'
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    name = Column(String)

    def __init__(self, symbol, name):
        self.symbol = symbol
        self.name = name


class Profile(Base):
    __tablename__ = 'profiles'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    sex = Column(String)
    address = Column(String)
    mail = Column(String)
    birthdate = Column(DateTime)

    def __init__(self, username, name, sex, address, mail, birthdate):
        self.username = username
        self.name = name
        self.sex = sex
        self.address = address
        self.mail = mail
        self.birthdate = birthdate
