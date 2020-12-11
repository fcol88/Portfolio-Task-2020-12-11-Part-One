import unittest
from app import Calculator

class AppTests(unittest.TestCase):

    def setUp(self):

        self.calculator = Calculator()

    def test_calculator_instantiates(self):
        
        self.assertIsInstance(self.calculator, Calculator)

    def test_add_sums_when_numbers(self):

        result = self.calculator.add(2,2)
        expected = 4
        self.assertEqual(result, expected)

    def test_add_rejects_when_string(self):

        self.assertRaises(ValueError, self.calculator.add, 2, "two")

    def test_subtract_subtracts_when_numbers(self):

        result = self.calculator.subtract(2,2)
        expected = 0
        self.assertEqual(result, expected)

    def  test_subtract_rejects_when_string(self):

        self.assertRaises(ValueError, self.calculator.subtract, 2, "two")

    def test_multiply_multiplies_when_numbers(self):

        result = self.calculator.multiply(2,2)
        expected = 4
        self.assertEqual(result, expected)

    def test_multiply_rejects_when_string(self):

        self.assertRaises(ValueError, self.calculator.add, 2, "two")

    def test_divide_divides_numbers_when_whole(self):

        result = self.calculator.divide(2,2)
        expected = 1
        self.assertEqual(result, expected)

    def test_divide_returns_decimal_when_not_whole(self):

        result = self.calculator.divide(3, 2)
        expected = 1.5
        self.assertEqual(result, expected)

    def test_divide_rejects_when_string(self):

        self.assertRaises(ValueError, self.calculator.divide, 2, "two")

    def test_divide_rejects_when_divisor_is_zero(self):

        self.assertRaises(ZeroDivisionError, self.calculator.divide, 2, 0)

    def test_simple_divide_returns_quotient_when_whole(self):

        result = self.calculator.simple_divide(4, 2)
        expected = 2
        self.assertEqual(result, expected)

    def test_simple_divide_returns_quotient_and_remainder_when_not_whole(self):

        result = self.calculator.simple_divide(5, 2)
        expected = 2, 1
        self.assertEqual(result, expected)

    def test_simple_divide_rejects_when_string(self):

        self.assertRaises(ValueError, self.calculator.simple_divide, 5, "two")

    def test_simple_divide_rejeects_when_divisor_is_zero(self):

        self.assertRaises(ZeroDivisionError, self.calculator.simple_divide, 5, 0)

if __name__ == "__main__":
    unittest.main()