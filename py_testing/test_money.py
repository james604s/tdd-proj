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

class Dollar:
        def __init__(self, amount):
            self.amount = amount

        def times(self, multiplier):
            return Dollar(self.amount * multiplier)

class TestMoney(unittest.TestCase): 
    def testMultiplication(self):
        fiver = Dollar(5)
        tenner = fiver.times(2)
        self.assertEqual(10, tenner.amount)
        
if __name__ == '__main__': 
    unittest.main()