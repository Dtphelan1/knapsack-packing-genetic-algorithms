import functools
import math
import logging
import configparser
from classes.I_Population import I_Population
from classes.SimpleIndividual import SimpleIndividual

# Config variables & logger
config = configparser.ConfigParser()
config.read('config/config.ini')
CULL_RATE = float(config.get("POPULATION", "CULL_RATE"))
LOGGER_NAME = config.get("LOGGER", "LOGGER_NAME")
logger = logging.getLogger(LOGGER_NAME + __name__)


class SimplePopulation(I_Population):
    def __init__(self, popSize, fitnessFn):
        self.popSize = popSize
        self.fitnessFn = fitnessFn
        self.generationNumber = 0
        self.popMembers = [SimpleIndividual() for i in range(popSize)]
        self.orderPopulation()

    def orderPopulation(self):
        self.popMembers.sort(
            key=self.fitnessFn,
            reverse=True
        )

    def nextGeneration(self):
        # Cull population - assumes population is sorted
        cullPoint = math.floor(self.popSize * CULL_RATE)
        self.popMembers = self.popMembers[:cullPoint]
        # For every pair of remaining population members
        newPopulation = []
        iterPop = iter(self.popMembers)
        for parent_1 in iterPop:
            # Mate with the next popMember
            parent_2 = next(iterPop)
            # If there is no next popMember, break
            if (parent_2 is None):
                break
            newPopulation.append(parent_1.mate(parent_2))
        self.popMembers += newPopulation
        # Maintain population sorting
        self.orderPopulation()
        self.generationNumber += 1

    def printGenerationReport(self):
        bestSolution = self.bestSolution()
        popAsWeights = [individual.weight() for individual in self.popMembers]
        logger.debug(f"popAsWeights - {popAsWeights}")
        popAsValues = [individual.value() for individual in self.popMembers]
        logger.debug(f"popAsValues - {popAsValues}")
        avgValue = sum(popAsValues) / self.popSize
        avgWeight = sum(popAsWeights) / self.popSize
        logging.info(f'''
        ================
        = Generation #{self.generationNumber + 1}
        ================
        Average Value: {avgValue}
        Average Weight: {avgWeight}
        Best Value: {bestSolution.value()}
        ''')

    def bestSolution(self):
        return self.popMembers[0]
