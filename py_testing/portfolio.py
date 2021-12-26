import functools
import operator
from money import Money

class Portfolio:
    def __init__(self): 
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)
    
    def evaluate(self, currency): 
        """
            1.If there are no failures, a new Money object with the correct amount and currency is returned
            2.If there are conversions failures, an Exception listing all the failed conversions is returned
        """
        total = functools.reduce(operator.add, map(lambda m: self.__convert(m, currency)), self.moneys) 
        total =0.0
        failures = []
        for m in self.moneys:
            try:
                total += self.__convert(m, currency)
            except KeyError as ke:
                failure.append(ke)
        
        if len(failures) == 0:
            return Money(total, currency)
        
        failureMessage = ",".join(f.args[0] for f in failures)
        raise Exception("Missing exchange rate(s):[" + failureMessage + "]")

    def __convert(self, aMoney, aCurrency): 
        if aMoney.currency == aCurrency:
            return aMoney.amount 
        else:
            key = aMoney.currency + '->' + aCurrency
            return aMoney.amount * exchangeRates[key]