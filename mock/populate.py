from mock import logger
# data generator class
from mock.generate import Generator
# sqlalchemy orm
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# os
import os

# get base dir
base_dir = os.path.dirname(os.path.realpath(__file__))

class RDBMS:
    pass

class SQLite:
    def __init__(self, data_types=['name', 'job', 'address', 'currency', 'profile'], data_size=10000, db_name="sinbad.mock.db"):
        # db name
        self.db_name = db_name
        # create db engine
        self.engine = create_engine("sqlite:///" + self.db_name)
        Session = scoped_session(
            sessionmaker(bind=self.engine, expire_on_commit=False)
        )
        # create db session
        self.session = Session()
        # data generator
        self.generator = Generator(types=data_types, data_size=data_size)
        # bind engine with generator models
        self.generator.models.Base.metadata.bind = self.engine
        # drop all tables
        self.generator.models.Base.metadata.drop_all()
        # create all models
        self.generator.models.Base.metadata.create_all()
    
    def store(self):
        # generate data
        data = self.generator.convert(to="db")
        # save each table generated
        for data_type in self.generator.types:
            # get type data
            type_data = data[data_type]
            # insert into db
            self.session.bulk_save_objects(type_data)
        
class FileStorage:
    def __init__(self, data_types=['name', 'job', 'address', 'currency', 'profile'], data_size=10000, dir_name="data", dir_path=None, file_types=["csv", "json", "parquet"]):
        logger.info("file storage init")
        # data generator
        self.generator = Generator(types=data_types, data_size=data_size)
        # file output type
        self.file_types = file_types
        # data dir
        self.data_dir_name = dir_name
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
        logger.info("storing to: %s" % data_dir)
        # generate data (dict of type [string]list where list is list of dfs
        # for each data type specified)
        data = self.generator.convert(to="f")
        # save each df generated
        for data_type in self.generator.types:
            for file_type in self.file_types:
                # get df
                df = data[data_type]
                # generate filename
                filename = os.path.join(data_dir, data_type + "." +  file_type)
                if file_type == "csv":
                    # save df
                    df.to_csv(filename)
                elif file_type == "json":
                    # save df
                    df.to_json(filename)
                elif file_type == "parquet":
                    df.to_parquet(filename)
                else:
                    print("no data found")