"""
    test_generate.py: test generator classes
"""
import pytest

# import generators
from mock.generate import Generator


def test_generator_init():
    """
    test generator class init method
    """
    # create generator
    generator = Generator(data_size=10)
    # assert generator types
    assert isinstance(generator, Generator)
    # assert generator db models exist
    assert generator.models is not None
    # assert generated & converted data initially
    # are empty
    assert len(generator.generated_data) == 0
    assert len(generator.converted_data_db) == 0
    assert generator.converted_data_df is None


def test_generator_init_invalid():
    """
    test generator class init method with invalid parameter values
    """
    # assert value error is raised
    with pytest.raises(ValueError):
        # create generator
        Generator(
            # size of data generated
            data_size=10,
            # invalid data type
            data_type="invalid",
        )


def test_generator_generate():
    """
    test generator class generate method
    """
    # create generator
    generator = Generator(data_size=10)
    # assert generator types
    assert isinstance(generator, Generator)
    # assert generator db models exist
    assert generator.models is not None
    # assert generated & converted data initially
    # are empty
    assert len(generator.generated_data) == 0
    assert len(generator.converted_data_db) == 0
    assert generator.converted_data_df is None
    # run generate method
    generator.generate()
    # assert generator types
    assert isinstance(generator, Generator)
    # assert generator db models exist
    assert generator.models is not None
    # assert generated data is not empty
    assert len(generator.generated_data) != 0
    assert len(generator.generated_data) == 10
    # assert converted data is empty w/o calling
    # convert method
    assert len(generator.converted_data_db) == 0
    assert generator.converted_data_df is None


def test_generator_convert():
    """
    test generator class convert method
    """
    # create generator
    generator = Generator(data_size=10)
    # assert generator types
    assert isinstance(generator, Generator)
    # assert generator db models exist
    assert generator.models is not None
    # assert generated & converted data initially
    # are empty
    assert len(generator.generated_data) == 0
    assert len(generator.converted_data_db) == 0
    assert generator.converted_data_df is None
    # run generate
    generator.generate()
    # assert generator types
    assert isinstance(generator, Generator)
    # assert generator db models exist
    assert generator.models is not None
    # assert generated data is not empty
    assert len(generator.generated_data) != 0
    # assert converted data is empty
    assert len(generator.converted_data_db) == 0
    assert generator.converted_data_df is None
    # run convert
    generator.convert(convert_to="db")
    # assert generator types
    assert isinstance(generator, Generator)
    # assert generator db models exist
    assert generator.models is not None
    # assert db conversion worked
    assert len(generator.generated_data) != 0
    assert len(generator.converted_data_db) != 0
    assert generator.converted_data_df is None
    # run convert
    generator.convert(convert_to="f")
    # assert generator types
    assert isinstance(generator, Generator)
    # assert generator db models exist
    assert generator.models is not None
    # assert file conversion worked
    assert len(generator.generated_data) != 0
    assert len(generator.converted_data_db) != 0
    assert generator.converted_data_df is not None
