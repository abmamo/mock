"""
    test_mock.py: tesk mock generators
"""
# path
import pathlib

# delete after tests finish
import shutil

# testing
import pytest

# import generator
from mock import SQLiteGenerator, FileGenerator


@pytest.fixture()
def test_data_dir():
    """
    create test data directory and delete it after
    tests finish running
    """
    # get the current file's directory
    current_path = pathlib.Path(__file__).parent.absolute()
    # create dir path
    test_data_dir = current_path.joinpath( # pylint: disable=redefined-outer-name
        "data"
    )
    # create dir
    test_data_dir.mkdir(parents=True, exist_ok=True)
    # yield
    yield test_data_dir
    # remove directory
    shutil.rmtree(test_data_dir)


def test_sqlite_default(
    test_data_dir,
):  # pylint: disable=redefined-outer-name,unused-argument
    """
    test sqlite data generator (w/o name)
    """

    # init sqlite generator
    sqlite_generator = SQLiteGenerator(data_size=10)
    # store data to dir
    sqlite_generator.store()
    # assert db exists in fs
    assert pathlib.Path("./mock.db").exists()
    # remove mock db
    pathlib.Path("./mock.db").unlink()


def test_sqlite_with_name(
    test_data_dir,
):  # pylint: disable=redefined-outer-name,unused-argument
    """
    test sqlite data generator with name of db specified
    """

    # init sqlite generator
    sqlite_generator = SQLiteGenerator(data_size=10)
    # store data to dir
    sqlite_generator.store(data_dir=test_data_dir, db_name="test.db")
    # assert
    assert test_data_dir.joinpath("test.db").exists()


def test_files_invalid_file_type():
    """
    test files data generator with invalid file types
    """

    # assert value error is raised
    with pytest.raises(ValueError):
        # init file generator
        FileGenerator(data_size=10, file_type="invalid")


def test_files_invalid_data_type():
    """
    test files data generator with invalid file types
    """

    # assert value error is raised
    with pytest.raises(ValueError):
        # init file generator
        FileGenerator(data_size=10, data_type="invalid")


def test_files_default(test_data_dir):  # pylint: disable=redefined-outer-name
    """
    test files data generator
    """

    # init params
    data_type = "profile"
    file_type = "csv"
    # init file generator
    file_generator = FileGenerator(
        data_size=1, file_type=file_type, data_type=data_type
    )
    # store data to dir
    file_generator.store(data_dir=test_data_dir)
    # assert file generated
    assert test_data_dir.joinpath(
        file_generator.data_type + "." + file_generator.file_type
    ).exists()


def test_files_with_name(test_data_dir):  # pylint: disable=redefined-outer-name
    """
    test files data generator with file names specified
    """

    # init file generator
    file_generator = FileGenerator(data_size=10)
    # store data to dir
    file_generator.store(data_dir=test_data_dir, file_name="random_name")
    # assert file generated
    assert test_data_dir.joinpath("random_name." + file_generator.file_type).exists()


def test_files_without_dir_name():
    """
    test files data generator without dir name
    """

    # init file generator
    file_generator = FileGenerator(data_size=10)
    # store data to dir
    file_generator.store(data_dir_name="nonexist", file_name="random_name")
    # assert file generated
    assert (
        pathlib.Path.cwd()
        .joinpath("nonexist")
        .joinpath("random_name." + file_generator.file_type)
        .exists()
    )

    shutil.rmtree(pathlib.Path.cwd().joinpath("nonexist"))
