# os
import os, sys
# logger
from mock import logger
# generator
from mock.generate import Generator
# sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# get base dir
base_dir = os.path.dirname(os.path.realpath(__file__))


class SQLite:
    """
        mock SQLite data generator. gets mock data using Generator class
        and bulk inserts it into a SQLite database using SQLAlchemy

        init params
            - data_types: list of data domains (limited to name, job, address, currency, profile)
            - data_size: size of data generated
            - db_name: name of SQLite database generated
    """
    def __init__(self, data_types=['name', 'job', 'address', 'currency', 'profile'], data_size=10000, db_name="sinbad.mock.db"):
        # db name
        self.db_name = db_name
        # data generator
        self.generator = Generator(types=data_types, data_size=data_size)

    def store(self, data_dir):
        """
            convert and store generated data in a SQLite database

            params:
                - data_dir: directory to store SQLite database in
            returns:
                - nothing
        """
        # create db engine using above name
        # generate filename
        if data_dir is not None:
            engine = create_engine("sqlite:///" + os.path.join(data_dir, self.db_name))
        else:
            engine = create_engine("sqlite:///" + self.db_name)
        # create scoped session
        Session = scoped_session(
            sessionmaker(bind=engine, expire_on_commit=False)
        )
        # init scoped session
        session = Session()
        # bind engine with generator models
        self.generator.models.Base.metadata.bind = engine
        # drop all tables (if they exist)
        self.generator.models.Base.metadata.drop_all()
        # recreate all models
        self.generator.models.Base.metadata.create_all()
        # generate data using generator created at init
        data = self.generator.convert(to="db")
        # save each table generated (determined by Generator)
        for data_type in self.generator.types:
            # get type data
            type_data = data[data_type]
            # insert into db
            session.bulk_save_objects(type_data)


class FileStorage:
    """
        mock file data generator. gets mock data using Generator class
        and saves it to specified file types using pandas

        init params
            - data_types: list of data domains (limited to name, job, address, currency, profile)
            - data_size: size of data generated
            - db_name: name of SQLite database generated
    """
    def __init__(self, data_types=['name', 'job', 'address', 'currency', 'profile'], data_size=10000, dir_name="data", dir_path=None, file_types=["csv", "json", "parquet"]):
        # data generator
        self.generator = Generator(types=data_types, data_size=data_size)
        # file output type
        self.file_types = file_types
        # data dir name
        self.data_dir_name = dir_name
        # data dir path
        if dir_path is None:
            # default data dir
            data_dir = os.path.join(base_dir, self.data_dir_name)
            # if it doesn't exist
            if not os.path.exists(data_dir):
                # create dir
                os.makedirs(data_dir)
            self.data_dir = data_dir
        else:
            self.data_dir = dir_path

    def store(self, data_dir):
        """
            convert and store generated data in various file formats
            (supported by pandas)

            params:
                - nothing
            returns:
                - nothing
        """
        # log
        logger.info("storing to: %s" % data_dir)
        # generate data (dict of type [string]list where list is list of dfs
        # for each data type specified)
        data = self.generator.convert(to="f")
        # save each df generated
        for data_type in self.generator.types:
            # log
            logger.info("storing type: %s" % data_type)
            # for each file type specified
            for file_type in self.file_types:
                # get df from generated data for particular type
                df = data[data_type]
                # generate filename
                filename = os.path.join(data_dir, data_type + "." + file_type)
                if file_type == "csv":
                    # save df
                    df.to_csv(filename)
                elif file_type == "json":
                    # save df
                    df.to_json(filename)
                elif file_type == "parquet":
                    df.to_parquet(filename)
                else:
                    # log
                    logger.error("invalid file type: %s" % file_type)
                    # exit
                    sys.exit()
