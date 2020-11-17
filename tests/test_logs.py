def test_setup_logger():
    """
        test function to configure logger
    """
    # import functions
    import logging
    from mock.logs import setup_logging
    # create logger
    logger = setup_logging(logging.getLogger(__name__))
    # assert logger type
    assert type(logger) == logging.Logger
