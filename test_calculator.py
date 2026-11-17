import unittest

class TestCalculator(unittest.TestCase):

import unittest
import calculator


class TestCalculator(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-3, 4), -12)
        self.assertEqual(calculator.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertAlmostEqual(calculator.divide(3, 1), 1 / 3)

        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(2, 0)

        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)

        with self.assertRaises(ValueError):
            calculator.logarithm(1, 8)

        with self.assertRaises(ValueError):
            calculator.logarithm(0, 8)

        with self.assertRaises(ValueError):
            calculator.logarithm(-2, 8)

    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(-3, -4), 5)
        self.assertAlmostEqual(calculator.hypotenuse(0, 0), 0)

    def test_sqrt(self):
        self.assertEqual(calculator.square_root(9), 3)
        self.assertEqual(calculator.square_root(0), 0)
        self.assertAlmostEqual(calculator.square_root(2), 2 ** 0.5)

        with self.assertRaises(ValueError):
            calculator.square_root(-1)


if __name__ == "__main__":
    unittest.main()

    ######### Partner 2
    # def test_add(self): # 3 assertions
    #     fill in code

    # def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    # def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code

    # def test_logarithm(self): # 3 assertions
    #     fill in code

    # def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
    
    ######## Partner 1
    # def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    # def test_hypotenuse(self): # 3 assertions
    #     fill in code

    # def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code
    ##########################

# Do not touch this
