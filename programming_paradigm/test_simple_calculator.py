import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        self.calc = SimpleCalculator()

# --- Renamed Test Cases to Match Checker Requirements ---

    def test_addition(self):
        """
        Test the add method covering positive, negative, and zero inputs.
        """
        # Positive numbers
        self.assertEqual(self.calc.add(5, 3), 8)
        # Negative numbers
        self.assertEqual(self.calc.add(-1, -4), -5)
        # Mixed signs
        self.assertEqual(self.calc.add(-10, 5), -5)
        # With zero
        self.assertEqual(self.calc.add(0, 7), 7)
        

    def test_subtraction(self):
        """
        Test the subtract method covering various input types.
        """
        # Standard subtraction
        self.assertEqual(self.calc.subtract(10, 4), 6)
        # Result is negative
        self.assertEqual(self.calc.subtract(4, 10), -6)
        # Subtraction involving negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5, -3), 8)


    def test_multiplication(self):
        """
        Test the multiply method covering positive, negative, and zero.
        """
        # Standard multiplication
        self.assertEqual(self.calc.multiply(6, 7), 42)
        # Negative results
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        # Double negative (positive result)
        self.assertEqual(self.calc.multiply(-5, -5), 25)
        # Multiplication by zero
        self.assertEqual(self.calc.multiply(100, 0), 0)


    def test_division(self):
        """
        Test the divide method covering standard division and division by zero.
        """
        # Standard division (float result)
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(1, 2), 0.5)
        # Division by negative
        self.assertEqual(self.calc.divide(10, -5), -2.0)
        # Edge case: division by zero (should return None as per the class spec)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))


if __name__ == '__main__':
    unittest.main()