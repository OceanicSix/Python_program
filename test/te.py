import calculator
import unittest

class testforclalulator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(calculator.addition(2,3),5)

    def test_multiplication(self):
        self.assertEqual(calculator.multiplication(2,5),10)

    def test_greater(self):
        self.assertTrue(calculator.greater(5,4))

if __name__ == '__main__':
    unittest.main()