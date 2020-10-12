class I_Individual():
    def __init__(self):
        self.genome = None

    def mate(self, i2):
        raise NotImplementedError

    def value(self):
        raise NotImplementedError

    def weight(self):
        raise NotImplementedError

    def isOverweight(self):
        raise NotImplementedError
