import os
import logging.config
import pathlib


def setup_logging(logger, std_level=logging.INFO, info_level=logging.INFO, error_level=logging.ERROR):
    """
        configure logger

        params:
            - logger: logging.Logger object
            - std_level: logging level for std out
            - info_level: logging level for info.log
            - error_level: logging level for error.log
        returns:
            - logger: configured logger object
    """
    # get the current file's directory
    current_path = pathlib.Path(__file__).parent.absolute()
    # define formatter
    formatter = logging.Formatter(
        "[%(asctime)s] - %(name)-25s %(levelname)-10s %(funcName)s:%(lineno)-18s   %(message)s"
    )
    # define stream handler
    std_handler = logging.StreamHandler()
    # add formatter to stream handler
    std_handler.setFormatter(formatter)
    # set level
    std_handler.setLevel(std_level)
    # add handler
    logger.addHandler(std_handler)
    # define file info handler
    file_info_handler = logging.handlers.RotatingFileHandler(
        os.path.join(current_path, "info.log"),
        maxBytes=1000000,
        backupCount=1
    )
    # set level
    file_info_handler.setLevel(info_level)
    # set formatter
    file_info_handler.setFormatter(formatter)
    # define file error handler
    file_error_handler = logging.handlers.RotatingFileHandler(
        os.path.join(current_path, "error.log"),
        maxBytes=1000000,
        backupCount=1
    )
    # set level
    file_error_handler.setLevel(error_level)
    # set formatter
    file_error_handler.setFormatter(formatter)
    # add handler to logger
    logger.addHandler(file_info_handler)
    logger.addHandler(file_error_handler)
    # return logger
    return logger
