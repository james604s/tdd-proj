import unittest
import operator
import functools

from money import Money
from portfolio import Portfolio
"""
1. Importing the unittest package, needed for the TestCase superclass '
2. Our test class, which must subclass the unittest.TestCase class 
3. Our method name must start with test to qualify as a test method 
4. Object representing “USD 5”. Dollar does not exist yet
5. Method under test: times — which also does not exist yet
6. Comparing actual value with expected value in a assertEqual statement

python py_testing/test_money.py                
"""

# class Dollar:
#     def __init__(self, amount):
#         self.amount = amount

#     def times(self, multiplier):
#         return Dollar(self.amount * multiplier)

class TestMoney(unittest.TestCase): 
    def testMultiplication(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD") 
        self.assertEqual(tenDollars, fiveDollars.times(2))
    
    def testDivision(self):
        originalMoney = Money(4002, "KRW") 
        expectedMoneyAfterDivision = Money(1000.5, "KRW") 
        self.assertEqual(expectedMoneyAfterDivision,originalMoney.divide(4))

    def testAddition(self):
        """
        1. We start with an empty Portfolio object.
        2. We then Add multiple Money object stoth is Portfolio.
        3. We ask the Portfolio to evaluate it self in aspec if iccurrency.
        4. Finally,the result of the evaluation should be a Money object with the correct amount and currency.
        """
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars) 
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portfolio.evaluate("USD")
        self.assertEqual(expectedValue, actualValue, "%s != %s"%(expectedValue, actualValue))

if __name__ == '__main__': 
    unittest.main()