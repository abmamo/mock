"""
    models.py: contains SQLAlchemy mock data models
"""
# sqlalchemy declarative base
from sqlalchemy.ext.declarative import declarative_base

# sqlalchemy column types
from sqlalchemy import Column, Integer, String, DateTime

# init sqlalchemy declarative base
Base = declarative_base()


class Person(Base):  # pylint: disable=too-few-public-methods
    """
    person db model
    """

    __tablename__ = "persons"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        """
        init person db instance
        """
        self.name = name


class Job(Base):  # pylint: disable=too-few-public-methods
    """
    job db model
    """

    __tablename__ = "jobs"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        """
        init job db instance
        """
        self.name = name


class Address(Base):  # pylint: disable=too-few-public-methods
    """
    address db model
    """

    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __init__(self, name):
        """
        init address db instance
        """
        self.name = name


class Currency(Base):  # pylint: disable=too-few-public-methods
    """
    currency db model
    """

    __tablename__ = "currencies"
    id = Column(Integer, primary_key=True)
    symbol = Column(String)
    name = Column(String)

    def __init__(self, symbol, name):
        """
        init currency db instance
        """
        self.symbol = symbol
        self.name = name


class Profile(Base):  # pylint: disable=too-few-public-methods
    """
    profile db model
    """

    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True)
    username = Column(String)
    name = Column(String)
    sex = Column(String)
    address = Column(String)
    mail = Column(String)
    birthdate = Column(DateTime)

    def __init__(
        self, username, name, sex, address, mail, birthdate
    ):  # pylint: disable=too-many-arguments
        """
        init profile db instance
        """
        self.username = username
        self.name = name
        self.sex = sex
        self.address = address
        self.mail = mail
        self.birthdate = birthdate
