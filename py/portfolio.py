
from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, bank, currency):
        """
            1.If there are no failures, a new Money object with the correct amount and currency is returned
            2.If there are conversions failures, an Exception listing all the failed conversions is returned
        """
        # total = functools.reduce(operator.add, map(lambda m: self.__convert(m, currency)), self.moneys) 
        
        total = Money(0, currency)
        failures = ""
        for m in self.moneys:
            c, k = bank.convert(m, currency)
            if k is None:
                total += c
            else:
                failures += k if not failures else "," + k
        if not failures:
            return total

        raise Exception("Missing exchange rate(s):[" + failures + "]")