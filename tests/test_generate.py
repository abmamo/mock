import pytest

def test_generator_init():
    """
        test generator class init method
    """
    # import dependencies
    from mock.generate import Generator
    # create generator
    generator = Generator(data_size=10)
    # assert generator types
    assert type(generator) == Generator
    # assert generator db models exist
    assert generator.models is not None
    # assert generated & converted data initially
    # are empty
    assert len(generator.all_data) == 0
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0

def test_generator_init_invalid():
    """
        test generator class init method with invalid parameter values
    """
    # import dependencies
    from mock.generate import Generator
    # assert value error is raised
    with pytest.raises(ValueError):
        # create generator
        generator = Generator(data_size=10, data_types=["invalid"])
    

def test_generator_generate():
    """
        test generator class generate method
    """
    # import dependencies
    from mock.generate import Generator
    # create generator
    generator = Generator(data_size=10)
    # assert generator type
    assert type(generator) == Generator
    # assert generator db models exist
    assert generator.models is not None
    # assert generated & converted data initially
    # are empty
    assert len(generator.all_data) == 0
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0
    # run generate method
    generator.generate()
    # assert generator type
    assert type(generator) == Generator
    # assert generator db models exist
    assert generator.models is not None
    # assert generated data is not empty
    assert len(generator.all_data) != 0
    # assert converted data is empty w/o calling
    # convert method
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0


def test_generator_convert():
    """
        test generator class convert method
    """
    # import dependencies
    from mock.generate import Generator
    # create generator
    generator = Generator(data_size=10)
    # assert
    assert type(generator) == Generator
    # assert generator db models exist
    assert generator.models is not None
    # assert generated & converted data initially
    # are empty
    assert len(generator.all_data) == 0
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0
    # run generate
    generator.generate()
    # assert
    assert type(generator) == Generator
    # assert generator db models exist
    assert generator.models is not None
    # assert generated data is not empty
    assert len(generator.all_data) != 0
    # assert converted data is empty
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0
    # run convert
    generator.convert(to="db")
    # assert
    assert type(generator) == Generator
    # assert generator db models exist
    assert generator.models is not None
    # assert db conversion worked
    assert len(generator.all_data) != 0
    assert len(generator.converted_data_db) != 0
    assert len(generator.converted_data_df) == 0
    # run convert
    generator.convert(to="f")
    # assert
    assert type(generator) == Generator
    # assert generator db models exist
    assert generator.models is not None
    # assert file conversion worked
    assert len(generator.all_data) != 0
    assert len(generator.converted_data_db) != 0
    assert len(generator.converted_data_df) != 0
