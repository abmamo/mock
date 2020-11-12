# logger
from mock import logger
# faker
from faker import Faker
# pandas
import pandas as pd
# db models
import mock.models as models
# tqdm
from tqdm import tqdm
# sys
import sys
# init faker
faker = Faker()


class Generator:
    """
        use faker to generate real-looking random data. the generated data can be names, jobs
        address, currencies, and profiles. the generated data can be a list of SQLAlchemy
        object (to store in a db) or a dataframe (to store to a file)

        init params:
            - types: list of data domains (limited to name, job, address, currency, profile)
            - data_size: size of data generated
    """
    def __init__(self, types=['name', 'job', 'address', 'currency', 'profile'], data_size=10000):
        # data domains
        self.types = types
        # num data items
        self.data_size = data_size
        # generated data in dict format
        # each type in self.type will have one
        self.all_data = {}
        # converted version of generated data above
        # could be sqlalchemy objects or dataframes
        # depending on the end result
        self.converted_data_db = {}
        self.converted_data_df = {}
        # db models
        self.models = models

    def generate(self):
        """
            generate mock data

            params:
                - none
            returns:
                - all_data: dict containing all generated data of the format [type]data
                            where type in self.types
        """
        # for each domain type given
        for data_type in self.types:
            # log
            logger.info("generating type: %s" % data_type)
            # init empty list to store generated domain data
            type_data = []
            # for given data size
            for _ in tqdm(range(self.data_size)):
                # use faker to generate fake dicts & append
                if data_type == 'name':
                    type_data.append(faker.name())
                elif data_type == 'job':
                    type_data.append(faker.job())
                elif data_type == 'address':
                    type_data.append(faker.address())
                elif data_type == 'currency':
                    # generate currency
                    currency = faker.currency()
                    # append dict
                    type_data.append({'symbol': currency[0], 'name': currency[1]})
                elif data_type == 'profile':
                    type_data.append(faker.simple_profile())
                else:
                    # log
                    logger.error("invalid type: %s" % data_type)
                    # exit
                    sys.exit()
            # add domain data to all data
            self.all_data[data_type] = type_data
        # return generated data
        return self.all_data

    def convert(self, to="db"):
        """
            convert generated data to appropriate format

            params:
                - to: destination (either "db" or "f")
            returns:
                - converted data
        """
        # if data hasn't been generated
        if not self.all_data:
            # generate first
            self.generate()
        # convert to db objects
        if to == "db":
            # for each domain type in all data
            for data_type in self.all_data:
                # log
                logger.info("converting type: %s" % data_type)
                # create associated sqlalchemy class
                # definition in models.py
                if data_type == "name":
                    # list to store sqlalchemy classes in
                    type_data = []
                    # add all names
                    for name in self.all_data[data_type]:
                        # create sqlalchemy object
                        type_data.append(models.Person(name))
                    self.converted_data_db[data_type] = type_data
                elif data_type == "job":
                    # list to store sqlalchemy classes in
                    type_data = []
                    # add all jobs
                    for name in self.all_data[data_type]:
                        # create sqlalchemy object
                        type_data.append(models.Job(name))
                    self.converted_data_db[data_type] = type_data
                elif data_type == "address":
                    # list to store sqlalchemy classes in
                    type_data = []
                    # add all addresses
                    for name in self.all_data[data_type]:
                        # create sqlalchemy object
                        type_data.append(models.Address(name))
                    self.converted_data_db[data_type] = type_data
                elif data_type == "currency":
                    # list to store sqlalchemy classes in
                    type_data = []
                    # add all currencies
                    for currency in self.all_data[data_type]:
                        # create sqlalchemy object
                        type_data.append(models.Currency(symbol=currency["symbol"], name=currency["name"]))
                    self.converted_data_db[data_type] = type_data
                elif data_type == "profile":
                    # list to store sqlalchemy classes in
                    type_data = []
                    # add all proiles
                    for profile in self.all_data[data_type]:
                        # create sqlalchemy object
                        type_data.append(models.Profile(username=profile["username"], name=profile["name"], sex=profile["sex"], address=profile["address"], mail=profile["mail"], birthdate=profile["birthdate"]))
                    self.converted_data_db[data_type] = type_data
                else:
                    print("invalid type: %s" % data_type)
            return self.converted_data_db
        elif to == "f":
            # for each domain
            for data_type in self.all_data:
                # log
                logger.info("converting type: %s" % data_type)
                # if it is a list we won't have keys to use as column names
                if isinstance(self.all_data[data_type][0], str):
                    # create df
                    df = pd.DataFrame(self.all_data[data_type], columns=[data_type])
                # if it is a dict we use keys to use as column names
                elif isinstance(self.all_data[data_type][0], dict):
                    df = pd.DataFrame.from_dict(self.all_data[data_type])
                else:
                    # log
                    logger.error("invalid data type: %s" % data_type)
                    # exit
                    sys.exit()
                # add dataframe to converted data
                self.converted_data_df[data_type] = df
            # return converted data
            return self.converted_data_df
