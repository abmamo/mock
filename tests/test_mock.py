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


def test_sqlite_default(test_data_dir):
    """
        test sqlite data generator (w/o name)
    """
    # import generator
    from mock import SQLiteGenerator
    # init sqlite generator
    sqlite_generator = SQLiteGenerator(data_size=10)
    # store data to dir
    sqlite_generator.store()
    # import path management lib
    import pathlib
    # assert db exists in fs
    assert pathlib.Path("./mock.db").exists()
    # remove mock db
    pathlib.Path("./mock.db").unlink()

def test_sqlite_with_name(test_data_dir):
    """
        test sqlite data generator with name of db specified
    """
    # import generator
    from mock import SQLiteGenerator
    # init sqlite generator
    sqlite_generator = SQLiteGenerator(data_size=10)
    # store data to dir
    sqlite_generator.store(data_dir=test_data_dir, db_name="test.db")
    # assert
    assert test_data_dir.joinpath("test.db").exists()

def test_files_invalid_type():
    """
        test files data generator with invalid file types
    """
    # import generator
    from mock import FileGenerator
    # invalid init params
    file_types = ["csv", "json", "xls", "parquet", "zoomy"]
    data_types = ["name", "job", "profile", "currency", "address"]
    # assert value error is raised
    with pytest.raises(ValueError):
        # init file generator
        file_generator = FileGenerator(
            data_size=10,
            file_types=file_types,
            data_types=data_types
        )


def test_files_default(test_data_dir):
    """
        test files data generator
    """
    # import generator
    from mock import FileGenerator
    # init params
    data_types = ["name", "job", "profile", "currency", "address"]
    # init file generator
    file_generator = FileGenerator(
        data_size=10,
        data_types=data_types
    )
    # store data to dir
    file_generator.store(data_dir=test_data_dir)
    # get expected files using init params
    import itertools
    expected_files = [data_type + "." + file_type for data_type, file_type in itertools.product(data_types, file_generator.file_types)]
    # for each expected file name
    for expected_file in expected_files:
        # assert file exists
        assert test_data_dir.joinpath(expected_file).exists()

def test_files_with_names(test_data_dir):
    """
        test files data generator with file names specified
    """
    # import generator
    from mock import FileGenerator
    # init params
    file_types = ["csv", "json", "xls", "parquet"]
    data_types = ["name", "job", "profile", "currency", "address"]
    # init file generator
    file_generator = FileGenerator(
        data_size=10,
        file_types=file_types,
        data_types=data_types
    )
    # store data to dir
    file_generator.store(data_dir=test_data_dir, file_name="random_name")
    # get expected files using init params
    import itertools
    expected_files = ["random_name." + file_type for file_type in file_types]
    # for each expected file name
    for expected_file in expected_files:
        # assert file exists
        assert test_data_dir.joinpath(expected_file).exists()


def test_files_without_dir_name():
    """
        test files data generator without dir name
    """
    # import generator
    from mock import FileGenerator
    # init params
    file_types = ["csv", "json", "xls", "parquet"]
    data_types = ["name", "job", "profile", "currency", "address"]
    # init file generator
    file_generator = FileGenerator(
        data_size=10,
        file_types=file_types,
        data_types=data_types,
    )
    # store data to dir
    file_generator.store(data_dir_name="nonexist", file_name="random_name")
    # get expected files using init params
    import itertools
    expected_files = ["random_name." + file_type for file_type in file_types]
    # path
    import pathlib
    # for each expected file name
    for expected_file in expected_files:
        # assert file exists
        assert pathlib.Path.cwd().joinpath("nonexist").joinpath(expected_file).exists()
    # rm test folders
    import shutil
    shutil.rmtree(pathlib.Path.cwd().joinpath("nonexist"))