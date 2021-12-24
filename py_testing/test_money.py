import unittest

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


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency
    
    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)
    
    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)
    
    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency


class TestMoney(unittest.TestCase): 
    def testMultiplicationInDollars(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD") 
        self.assertEqual(tenDollars, fiveDollars.times(2))
    
    def testMultiplicationInEuros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR") 
        self.assertEqual(twentyEuros, tenEuros.times(2))
    
    def testDivision(self):
        originalMoney = Money(4002, "KRW") 
        expectedMoneyAfterDivision = Money(1000.5, "KRW") 
        self.assertEqual(expectedMoneyAfterDivision,originalMoney.divide(4))

if __name__ == '__main__': 
    unittest.main()