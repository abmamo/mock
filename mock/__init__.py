# os
import os
# logging
import logging
# set up logging before importing sub modules
from mock.logs import setup_logging
# configure logger
logger = setup_logging(logging.getLogger(__name__))
# generator
from mock.generate import Generator
# sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# get base dir
base_dir = os.path.dirname(os.path.realpath(__file__))


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
            data_size=10000,
            db_name="mock.db"):
        # SQLite db name
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
        # if data dir specified
        if data_dir is not None:
            # create sqlite db in data dir
            engine = create_engine(
                "sqlite:///" + os.path.join(data_dir, self.db_name)
            )
        # if no data specified
        else:
            # create sqlite db in current working dir
            engine = create_engine("sqlite:///" + self.db_name)
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
        for data_type in self.generator.types:
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
            # data dir name
            dir_name="data",
            # data dir path
            dir_path=None,
            # file types to generate
            file_types=["csv", "json", "parquet", "xlsx"]):
        # init data generator
        self.generator = Generator(types=data_types, data_size=data_size)
        # file types to generate
        self.file_types = file_types
        # data dir name
        self.data_dir_name = dir_name
        # if no data dir path specified
        if dir_path is None:
            # default data dir
            data_dir = os.path.join(base_dir, self.data_dir_name)
            # if it doesn't exist
            if not os.path.exists(data_dir):
                # create dir
                os.makedirs(data_dir)
            # set data dir
            self.data_dir = data_dir
        # if data dir specified
        else:
            # set data dir
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
        # converted generated data to form (dict of type [string]list
        # where list is list of dfs for each data type specified)
        data = self.generator.convert(to="f")
        # save each df generated
        for data_type in self.generator.types:
            # log
            logger.info("storing type/domain: %s" % data_type)
            # for each file type specified
            for file_type in self.file_types:
                # get df from generated data for particular type
                df = data[data_type]
                # generate filename
                filename = os.path.join(data_dir, data_type + "." + file_type)
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
                elif file_type == "xlsx":
                    # save df to excel
                    df.to_excel(filename)
                else:
                    # log
                    logger.error("invalid file type: %s" % file_type)
                    # exit
                    return
