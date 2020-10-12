import random
import logging
import configparser
from classes.I_Individual import I_Individual
from classes.SimpleGenome import SimpleGenome

# Config variables
config = configparser.ConfigParser()
config.read('config/config.ini')
MUTATION_RATE = float(config.get('INDIVIDUAL', 'MUTATION_RATE'))
LOGGER_NAME = config.get("LOGGER", "LOGGER_NAME")
logger = logging.getLogger(LOGGER_NAME + __name__)


class SimpleIndividual(I_Individual):
    def __init__(self, genome=None):
        self.genome = genome
        if genome is None:
            self.genome = SimpleGenome()
        logger.debug("self.genome after constructor")
        logger.debug(self.genome)

    def __str__(self):
        return str(self.genome)

    def mate(self, i2):
        crossed_over_genome = self.genome.crossover(i2.genome)
        offspring = SimpleIndividual(crossed_over_genome)
        if (random.random() > MUTATION_RATE):
            offspring.genome.mutate()
        return offspring

    def value(self):
        return self.genome.value()

    def weight(self):
        return self.genome.weight()

    def isOverweight(self):
        return self.genome.isOverweight()
