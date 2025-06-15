import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Initialize calculator before each test."""
        self.calc = SimpleCalculator()

    # Addition Tests
    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-4, -6), -10)
        self.assertEqual(self.calc.add(0, 0), 0)

    # Subtraction Tests
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(0, 7), -7)

    # Multiplication Tests
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(0, 99), 0)
        self.assertEqual(self.calc.multiply(-3, -2), 6)

    # Division Tests
    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertIsNone(self.calc.divide(10, 0))  # Division by zero

    # Optional: Float precision handling
    def test_division_float_precision(self):
        self.assertAlmostEqual(self.calc.divide(7, 3), 2.3333, places=4)

if __name__ == "__main__":
    unittest.main()
