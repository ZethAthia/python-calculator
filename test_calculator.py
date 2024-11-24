import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add_swap(self):
        self.assertEqual(self.calc.add(2, 1), 3)
    def test_add_negative(self):
        self.assertEqual(self.calc.add(1, -2), -1)
    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
    def test_sub_negative(self):
        self.assertEqual(self.calc.subtract(1, -2), 3)
    def test_mul_zero(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)
    def test_mul_negative(self):
        self.assertEqual(self.calc.multiply(20, -2), -40)
    def test_div_negative(self):
        self.assertEqual(self.calc.divide(20, -2), -10)
    def test_div_negative2(self):
        self.assertEqual(self.calc.divide(-20, -2), 10)
    def test_mod_negative_dividend(self):
        self.assertEqual(self.calc.modulo(-10, 3), 2)
    def test_mod_negative_modulus(self):
        self.assertEqual(self.calc.modulo(10, -3), -2)

    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main(verbosity=2)