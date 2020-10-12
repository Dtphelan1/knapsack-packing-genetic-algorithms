# from classes.Logger import logging
import argparse
import configparser
import logging
# Initializes logger config on load
import classes.Logger
from classes.SimplePopulation import SimplePopulation

# Config variables & logger
config = configparser.ConfigParser()
config.read('config/config.ini')
MAX_GENERATIONS = int(config.get("APP", "MAX_GENERATIONS"))
POPULATION_SIZE = int(config.get("APP", "POPULATION_SIZE"))
PRINT_FREQUENCY = int(config.get("APP", "PRINT_FREQUENCY"))
LOGGER_NAME = config.get("LOGGER", "LOGGER_NAME")
logger = logging.getLogger(LOGGER_NAME + __name__)


def fitnessFn(individual):
    return individual.value() if not individual.isOverweight() else 0,


def fitnessFnDensityBased(individual):
    return (individual.value() / individual.weight()) if not (individual.isOverweight() or individual.weight() == 0) else 0,


def main():
    pop = SimplePopulation(POPULATION_SIZE, fitnessFn)
    fittest_solution = None
    logger.info("Initialized population, beginnning new generations")
    for i in range(MAX_GENERATIONS):
        logger.debug(f"Generation {i + 1}")
        # Check the best population member
        fittest_solution = pop.bestSolution()
        # print a report of the every 25th generation
        if ((i + 1) % PRINT_FREQUENCY == 0):
            pop.printGenerationReport()
        # Make the next generation
        pop.nextGeneration()
    logger.info(f" --- Fittest population member --- ")
    logger.info(fittest_solution)
    logger.info(f" ------ ")


if __name__ == "__main__":
    main()
