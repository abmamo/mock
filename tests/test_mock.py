import pytest


@pytest.fixture()
def test_data_dir():
    """
        create test data directory and delete it after
        tests finish running
    """
    # create data dir
    import pathlib
    # get the current file's directory
    current_path = pathlib.Path(__file__).parent.absolute()
    # create dir path
    test_data_dir = current_path.joinpath("data")
    # create dir
    test_data_dir.mkdir(parents=True, exist_ok=True)
    # yield
    yield test_data_dir
    # delete after tests finish
    import shutil
    # remove directory
    shutil.rmtree(test_data_dir)


def test_sqlite(test_data_dir):
    """
        test sqlite data generator
    """
    # import generator
    from mock import SQLiteGenerator
    # init sqlite generator
    sqlite_generator = SQLiteGenerator(data_size=10, db_name="test.db")
    # store data to dir
    sqlite_generator.store(data_dir=test_data_dir)
    # assert
    assert test_data_dir.joinpath("test.db").exists()


def test_files(test_data_dir):
    """
        test files data generator
    """
    # import generator
    from mock import FileGenerator
    # init params
    file_types = ["csv", "json", "xlsx", "parquet"]
    data_types = ["name", "job", "profile", "currency", "address"]
    # init file generator
    file_generator = FileGenerator(
        data_size=10,
        file_types=file_types,
        data_types=data_types
    )
    # store data to dir
    file_generator.store(data_dir=test_data_dir)
    # get expected files using init params
    import itertools
    expected_files = [data_type + "." + file_type for data_type, file_type in itertools.product(data_types, file_types)]
    # for each expected file name
    for expected_file in expected_files:
        # assert file exists
        assert test_data_dir.joinpath(expected_file).exists()
