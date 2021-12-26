import functools
import operator
from money import Money

class Portfolio:
    def __init__(self): 
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)
    
    def evaluate(self, currency): 
        total = functools.reduce(operator.add, map(lambda m: self.__convert(m, currency)), self.moneys) 
        return Money(total, currency)

    def __convert(self, aMoney, aCurrency): 
        if aMoney.currency == aCurrency:
            return aMoney.amount 
        else:
            return aMoney.amount * 1.2