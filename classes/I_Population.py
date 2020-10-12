class I_Population():
    def __init__(self, popSize=0, fitnessFn=None):
        self.popMembers = []

    def nextGeneration(self):
        raise NotImplementedError

    def orderPopulation(self):
        raise NotImplementedError

    def bestSolution(self):
        raise NotImplementedError

    def printGenerationReport(self):
        raise NotImplementedError
