import unittest
from simple_calculator import SimpleCalculator 

class TestSimpleCalculator(unittest.TestCase):
    """
    Unit tests for the SimpleCalculator class.
    """

    def setUp(self):
        """Set up the SimpleCalculator instance before each test method runs."""
        self.calc = SimpleCalculator()

    # --- Test Cases for add method ---
    def test_addition_positive_numbers(self):
        """Test the addition of two positive numbers."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(100, 200), 300)

    def test_addition_negative_numbers(self):
        """Test the addition involving negative numbers."""
        self.assertEqual(self.calc.add(-1, -4), -5)
        self.assertEqual(self.calc.add(-10, 5), -5)

    def test_addition_with_zero(self):
        """Test the addition involving zero."""
        self.assertEqual(self.calc.add(0, 7), 7)
        self.assertEqual(self.calc.add(-7, 0), -7)

    # --- Test Cases for subtract method ---
    def test_subtraction_positive_numbers(self):
        """Test the subtraction of two positive numbers."""
        self.assertEqual(self.calc.subtract(10, 4), 6)
        self.assertEqual(self.calc.subtract(4, 10), -6)

    def test_subtraction_negative_numbers(self):
        """Test subtraction involving negative numbers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    # --- Test Cases for multiply method ---
    def test_multiplication_standard(self):
        """Test multiplication of standard numbers."""
        self.assertEqual(self.calc.multiply(6, 7), 42)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-5, -5), 25)

    def test_multiplication_by_zero(self):
        """Test multiplication when one factor is zero."""
        self.assertEqual(self.calc.multiply(100, 0), 0)
        self.assertEqual(self.calc.multiply(0, -50), 0)

    # --- Test Cases for divide method ---
    def test_division_standard(self):
        """Test normal division returning a float."""
        self.assertEqual(self.calc.divide(10, 5), 2.0)
        self.assertEqual(self.calc.divide(1, 2), 0.5)

    def test_division_by_zero(self):
        """Test the edge case: division by zero."""
        # The provided class returns None for division by zero
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))

if __name__ == '__main__':
    unittest.main()