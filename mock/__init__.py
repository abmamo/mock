# logging
import logging
# set up logging before importing sub modules
from mock.logs import setup_logging
# configure logging
logger = setup_logging(logging.getLogger(__name__))