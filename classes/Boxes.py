from pathlib import Path
import json
import configparser
import logging

# Config variables & logger
config = configparser.ConfigParser()
config.read('config/config.ini')
JSON_PATH = config.get('BOXES', 'JSON_PATH')
WEIGHT_LIMIT = int(config.get('BOXES', 'WEIGHT_LIMIT'))
LOGGER_NAME = config.get("LOGGER", "LOGGER_NAME")
logger = logging.getLogger(LOGGER_NAME + __name__)


class Boxes():
    data = []
    with Path(JSON_PATH).open() as json_file:
        logger.info(f"loading JSON data from {JSON_PATH}")
        data = json.load(json_file)
    logger.debug("data post load")
    logger.debug(data)

    @classmethod
    def getBoxValue(cls, ind):
        return cls.data[ind]["value"]

    @classmethod
    def getBoxWeight(cls, ind):
        return cls.data[ind]["weight"]

    @classmethod
    def getBoxesValue(cls, boolFilter):
        return [box["value"] for i, box in enumerate(cls.data) if boolFilter[i]]

    @classmethod
    def getBoxesWeight(cls, boolFilter):
        return [box["weight"] for i, box in enumerate(cls.data) if boolFilter[i]]

    @classmethod
    def isSelectionOverweight(cls, boolFilter):
        return sum([box["weight"] for i, box in enumerate(Boxes.data) if boolFilter[i]]) > WEIGHT_LIMIT
