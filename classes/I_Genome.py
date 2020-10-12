class I_Genome():
    def __init__(self):
        self.alleles = []

    def mutate(self):
        raise NotImplementedError

    def crossover(self, g2):
        raise NotImplementedError

    def value(self):
        raise NotImplementedError

    def weight(self):
        raise NotImplementedError

    def isOverweight(self):
        raise NotImplementedError
