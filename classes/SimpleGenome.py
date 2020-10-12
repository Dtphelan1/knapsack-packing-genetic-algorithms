import random
import math
import configparser
import logging
from classes.I_Genome import I_Genome
from classes.Boxes import Boxes

# Config variables & logger
config = configparser.ConfigParser()
config.read('config/config.ini')
LOGGER_NAME = config.get("LOGGER", "LOGGER_NAME")
logger = logging.getLogger(LOGGER_NAME + __name__)


class SimpleGenome(I_Genome):
    NEWLINE = "\n"

    def __init__(self, alleles=None):
        self.alleles = alleles
        if alleles is None:
            self.alleles = [bool(random.getrandbits(1)) for elem in Boxes.data]
        logger.debug("self.alleles after constructor")
        logger.debug(self.alleles)

    def __str__(self):
        total_str = ""
        total_str += f"Total Value: {self.value()}{self.NEWLINE}"
        total_str += f"Total Weight: {self.weight()}{self.NEWLINE}"
        total_str += f"Boxes included:{self.NEWLINE}"
        max_width = int(len(self.alleles) / 10) + 1
        for (i, allele) in enumerate(self.alleles):
            if allele:
                total_str += f" - #{str(i).rjust(max_width)}, Value: {Boxes.getBoxValue(i)}, Weight: {Boxes.getBoxWeight(i)}{self.NEWLINE}"
        return total_str

    def mutate(self):
        index = random.choice(range(len(self.alleles)))
        self.alleles[index] = not self.alleles[index]

    def crossover(self, g2):
        if (len(self.alleles) != len(g2.alleles)):
            raise Exception("P1 and P2 genomes are not identical in length")
        crossoverPoint = random.choice(range(len(self.alleles)))
        return SimpleGenome(self.alleles[:crossoverPoint] + g2.alleles[crossoverPoint:])

    def value(self):
        return sum(Boxes.getBoxesValue(self.alleles))

    def weight(self):
        return sum(Boxes.getBoxesWeight(self.alleles))

    def isOverweight(self):
        return Boxes.isSelectionOverweight(self.alleles)
