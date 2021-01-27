### logging config ###
# logging
import logging
# os / path
import os
from os import path
# config from .cfg file
from logging.config import fileConfig
# log dir (same as wherever this file is)
log_dir = path.dirname(path.abspath(__file__))
# get logging config path (same dir as this file)
logging_config_path = path.join(log_dir, 'logging.cfg')
# configure logging from file
fileConfig(logging_config_path)
# suppress logs from faker
logging.getLogger("faker.factory").setLevel(logging.WARNING)
# create module logger
logger = logging.getLogger('mock')
# set default logging to WARNING
logger.setLevel(logging.WARNING)
### data generation ###
# generator
from mock.generate import Generator
# sqlalchemy (sqlite orm)
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


class SQLiteGenerator:
    """
        mock SQLite data generator. generates mock data using the Generator
        class and bulk inserts it into a SQLite database using SQLAlchemy

        init params
            - data_types: list of data domains
                          (limited to name, job, address, currency, profile)
            - data_size: size of data generated
            - db_name: name of SQLite database generated
    """
    def __init__(
            self,
            data_types=['name', 'job', 'address', 'currency', 'profile'],
            data_size=10000):
        # init data generator
        self.generator = Generator(data_types=data_types, data_size=data_size)

    def store(self, data_dir=None, db_name="mock.db"):
        """
            convert and store generated data in a SQLite database

            params:
                - data_dir: directory to store SQLite database in
            returns:
                - nothing
        """
        # if data dir specified
        if data_dir is not None:
            # create sqlite db in data dir
            engine = create_engine(
                "sqlite:///" + os.path.join(data_dir, db_name)
            )
        # if no data specified
        else:
            # create sqlite db in current working dir
            engine = create_engine("sqlite:///" + db_name)
        # create scoped sqlalchemy session
        Session = scoped_session(
            sessionmaker(bind=engine, expire_on_commit=False)
        )
        # init scoped sqlalchemy session
        session = Session()
        # bind engine to generator faker models
        self.generator.models.Base.metadata.bind = engine
        # drop all tables (if they exist)
        self.generator.models.Base.metadata.drop_all()
        # recreate all tables
        self.generator.models.Base.metadata.create_all()
        # generate & convert data using generator
        data = self.generator.convert(to="db")
        # save each table generated for each data type/domain
        for data_type in self.generator.data_types:
            # get data type / domain
            type_data = data[data_type]
            # bulk insert into db
            session.bulk_save_objects(type_data)


class FileGenerator:
    """
        mock file data generator. gets mock data using Generator class
        and converts it to specified file types using pandas

        init params
            - data_types: list of data domains
                          (limited to name, job, address, currency, profile)
            - data_size: size of data generated
            - db_name: name of SQLite database generated
    """
    def __init__(
            self,
            # data types / domains
            data_types=['name', 'job', 'address', 'currency', 'profile'],
            # size of data generated
            data_size=10000,
            # file types to generate
            file_types=None):
        # supported file types
        self.supported_file_types = ["csv", "json", "parquet", "xls"]
        # if file types is not set use default
        if file_types is None:
            file_types = self.supported_file_types
        # check file types are valid
        if not all(file_type in self.supported_file_types for file_type in file_types):
            # raise error
            raise ValueError("invalid value: file_types. mock only supports: %s" % str(self.supported_file_types))
        # file types are all valid
        else:
            # file types to generate
            self.file_types = file_types
            # init data generator
            self.generator = Generator(data_types=data_types, data_size=data_size)
        

    def store(self, data_dir_name="data", data_dir=None, file_name=None):
        """
            convert and store generated data in various file formats
            (supported by pandas)

            params:
                - data_dir: directory to save generated files to
                - file_name: name of file to use to save generated files
            returns:
                - nothing
        """
        # if no data dir path specified
        if data_dir is None:
            # base dir
            base_dir = os.getcwd()
            # default data dir
            data_dir = os.path.join(base_dir, data_dir_name)
            # if it doesn't exist
            if not os.path.exists(data_dir):
                # create dir
                os.makedirs(data_dir)
            # set data dir
            data_dir = data_dir
        # converted generated data to form (dict of type [string]list
        # where list is list of dfs for each data type specified)
        data = self.generator.convert(to="f")
        # save each df generated
        for data_type in self.generator.data_types:
            # log
            logger.info("storing type/domain: %s" % data_type)
            # for each file type specified
            for file_type in self.file_types:
                # get df from generated data for particular type
                df = data[data_type]
                # if file name specified
                if file_name is not None:
                    # generate file path using specified file name + data dir + file type
                    filename = os.path.join(data_dir, file_name + "." + file_type)
                else:
                    # generate file path using specified data dir + default file names + file type
                    filename = os.path.join(data_dir, data_type + "." + file_type)
                # log
                logger.info("storing to: %s" % filename)
                # csv
                if file_type == "csv":
                    # save df to csv
                    df.to_csv(filename)
                # json
                elif file_type == "json":
                    # save df to json
                    df.to_json(filename)
                # parquet
                elif file_type == "parquet":
                    # save df to parquet
                    df.to_parquet(filename)
                # excel
                elif file_type == "xls":
                    # save df to excel
                    df.to_excel(filename)