


import unittest
import calculator



class TestForSum(unittest.TestCase):
    # all function must start with test
    #valid test case
    def test_sum_valid(self):
        self.assertEqual(calculator.test_add_sum(1, 2), 3)

    def test_sum_invalid(self):
        self.assertEqual(calculator.test_add_sum('a','b'),-1,'something wrong')



    #invalid test case

    #boundary case test

class testagain(unittest.TestCase):
    def testsum(self):
        self.assertEqual(calculator.test_add_sum(3,2),5)


# if __name__ == '__main__':
#
#     unittest.main()
t=TestForSum()
print('d')




