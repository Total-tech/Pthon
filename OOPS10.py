from abc import ABCMeta,abstractmethod

class Shapes(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class rectangle:
    type = "quadriletarel"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth