"""
    mock: mock module
"""
# os / path
import os

# logging
import logging

# logging config
from logging.config import dictConfig

# sqlalchemy (sqlite orm)
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

# generator
from mock.generate import Generator

# config obj
from mock.config import LOGGING_DICT as logging_cfg

# configure logging from dict
dictConfig(logging_cfg)
# suppress logs from faker
logging.getLogger("faker.factory").setLevel(logging.WARNING)
# create module logger
logger = logging.getLogger("mock")


class SQLiteGenerator:  # pylint: disable=too-few-public-methods
    """
    mock SQLite data generator. generates mock data using the Generator
    class and bulk inserts it into a SQLite database using SQLAlchemy

    init params
        - data_types: list of data domains
                      (limited to name, job, address, currency, profile)
        - data_size: size of data generated
        - db_name: name of SQLite database generated
    """

    def __init__(self, data_type="profile", data_size=10000):
        # init data generator
        self.generator = Generator(data_type=data_type, data_size=data_size)

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
            engine = create_engine("sqlite:///" + os.path.join(data_dir, db_name))
        # if no data specified
        else:
            # create sqlite db in current working dir
            engine = create_engine("sqlite:///" + db_name)
        # create scoped sqlalchemy session
        Session = scoped_session(  # pylint: disable=invalid-name
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
        data = self.generator.convert(convert_to="db")
        # bulk insert into db
        session.bulk_save_objects(data)


class FileGenerator:  # pylint: disable=too-few-public-methods
    """
    mock file data generator. gets mock data using Generator class
    and converts it to specified file types using pandas
    """

    def __init__(
        self,
        # data types / domains
        data_type="profile",
        # size of data generated
        data_size=1000,
        # file types to generate
        file_type="csv",
    ):
        """
        init params
            - data_types: list of data domains
                        (limited to name, job, address, currency, profile)
            - data_size: size of data generated
            - db_name: name of SQLite database generated
        """
        # supported file types
        self.supported_file_types = ["csv", "json", "parquet", "xls"]
        # supported data types
        self.supported_data_types = ["name", "job", "address", "currency", "profile"]
        # check file type is supported
        if file_type not in self.supported_file_types:
            # raise error
            raise ValueError(
                "invalid file_type: %s. mock supports: %s"
                % (str(file_type), str(self.supported_file_types))
            )
        # check data type is supported
        if data_type not in self.supported_data_types:
            # raise error
            raise ValueError(
                "invalid data_type: %s. mock supports: %s"
                % (str(file_type), str(self.supported_data_types))
            )
        # data type
        self.data_type = data_type
        # file type
        self.file_type = file_type
        # init data generator
        self.generator = Generator(data_type=data_type, data_size=data_size)

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
        # converted generated data to form (dict of type [string]list
        # where list is list of dfs for each data type specified)
        df = self.generator.convert(convert_to="f")  # pylint: disable=invalid-name
        # log
        logger.info("storing data type: %s", str(self.data_type))
        # if file name specified
        if file_name is not None:
            # generate file path using specified file name + data dir + file type
            filename = os.path.join(data_dir, file_name + "." + self.file_type)
        else:
            # generate file path using specified data dir + default file names + file type
            filename = os.path.join(data_dir, self.data_type + "." + self.file_type)
        # log
        logger.info("storing to: %s", str(filename))
        # csv
        if self.file_type == "csv":
            # save df to csv
            df.to_csv(filename)
        # json
        elif self.file_type == "json":
            # save df to json
            df.to_json(filename)
        # parquet
        elif self.file_type == "parquet":
            # save df to parquet
            df.to_parquet(filename)
        # excel
        elif self.file_type == "xls":
            # save df to excel
            df.to_excel(filename)
