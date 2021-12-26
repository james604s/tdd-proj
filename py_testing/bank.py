
from money import Money


class Bank:
    """
1.The Bank requires Money as a dependency
2.Initializing empty dictionary in __init__ method
3.Forming a key to store the exchange rate
4.This convert method resembles the __convert method in the Portfolio class
5.Creating a new Money object when currencies are the same 
6.raising an Exception when conversion fails                 
    """
    def __init__(self):
        self.exchangeRates = {}

    def addExchangeRate(self, currencyFrom, currencyTo, rate):
        key = currencyFrom + "->" + currencyTo
        self.exchangeRates[key] = rate

    def convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency), None

        key = aMoney.currency + "->" + aCurrency
        if key in self.exchangeRates:
            return Money(aMoney.amount * self.exchangeRates[key], aCurrency), None

        return None, key