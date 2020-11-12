def test_generator_init():
    """
        test generator class init method
    """
    # import dependencies
    from mock.generate import Generator
    # create generator
    generator = Generator(data_size=10)
    # assert
    assert type(generator) == Generator
    assert generator.models is not None
    assert len(generator.all_data) == 0
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0

def test_generator_generate():
    """
        test generator class generate method
    """
    # import dependencies
    from mock.generate import Generator
    # create generator
    generator = Generator(data_size=10)
    # assert
    assert type(generator) == Generator
    assert generator.models is not None
    assert len(generator.all_data) == 0
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0
    # run generate
    generator.generate()
    # assert
    assert type(generator) == Generator
    assert generator.models is not None
    assert len(generator.all_data) != 0
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
    assert generator.models is not None
    assert len(generator.all_data) == 0
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0
    # run generate
    generator.generate()
    # assert
    assert type(generator) == Generator
    assert generator.models is not None
    assert len(generator.all_data) != 0
    assert len(generator.converted_data_db) == 0
    assert len(generator.converted_data_df) == 0
    # run convert
    generator.convert(to="db")
    # assert
    assert type(generator) == Generator
    assert generator.models is not None
    assert len(generator.all_data) != 0
    assert len(generator.converted_data_db) != 0
    assert len(generator.converted_data_df) == 0
    # run convert
    generator.convert(to="f")
    # assert
    assert type(generator) == Generator
    assert generator.models is not None
    assert len(generator.all_data) != 0
    assert len(generator.converted_data_db) != 0
    assert len(generator.converted_data_df) != 0

