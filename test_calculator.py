# https://github.com/Ethan-Huang-UF/lab11-KK-EH.git

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 1), -3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(0, 0), 0)
    # ##########################

    ######## Partner 1
    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-3, 4), -12)
        self.assertEqual(mul(5, 0), 0)

    def test_divide(self):  # 3 assertions
        self.assertEqual(div(2, 10), 5)
        self.assertEqual(div(4, 10), 2.5)
        self.assertEqual(div(-3, 9), -3)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(5, 1), 0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(0, 5)
    # ##########################

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    def test_hypotenuse(self):  # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(5, 12), 13)
        self.assertEqual(hypotenuse(8, 15), 17)

    def test_sqrt(self):  # 3 assertions
        # Test for invalid argument
        with self.assertRaises(ValueError):
            square_root(-4)
        # Test basic function
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()
