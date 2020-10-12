import logging
import configparser

# Config variables
config = configparser.ConfigParser()
config.read('config/config.ini')
LOGGER_NAME = config.get("LOGGER", "LOGGER_NAME")

# Logger setup
FORMAT = "%(levelname)s:%(module)s:%(lineno)d - %(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger(LOGGER_NAME)
