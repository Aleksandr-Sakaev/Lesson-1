#task 2:
from abc import ABC, abstractmethod

class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @property
    def cost(self):
        return f'Amount of fabric spent: {self.param / 6.5 + 0.5 + 2*self.param +0.3:.2f}'

    @abstractmethod
    def abstr(self):
        return 'abstract'

class Coat(Clothes):
    def cost(self):
        return f'For sewing a coat you need: {self.param /6.5 + 0.5 :.2f} fabrics'

    def abstr(self):
        return 'abstract'

class Costume(Clothes):
    def cost(self):
        return f'To sew a suit you need: {2*self.param + 0.3 :.2f} fabrics'

    def abstr(self):
        pass

coat = Coat(300)
costum = Costume(120)
print(coat.cost())
print(costum.cost())
print(coat.abstr())

