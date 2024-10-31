"""
Weight Unit Test.

Spyder Editor.

Created on Thu Oct 31 01:14:14 2024
@author: BRICE NELSON
"""
import unittest
from weight import Weight  # Adjust the import based on file structure


class TestWeightConversions(unittest.TestCase):
    """
    Unit tests for Weight conversion methods in the Weight class.

    Each test verifies the correct conversion between kilograms (kg),
    pounds (lb), grams (g), and ounces (oz) for a given input.
    """

    def setUp(self):
        """Create an instance of the Weight class before each test."""
        self.converter = Weight()

    def test_kg_to_lb(self):
        """Test conversion from kilograms to pounds."""
        weight_in_kg = 1.0
        expected_lb = 2.20
        self.assertAlmostEqual(
            self.converter.kg_to_lb(weight_in_kg), expected_lb, places=2
        )

    def test_kg_to_g(self):
        """Test conversion from kilograms to grams."""
        weight_in_kg = 1.0
        expected_g = 1000.00
        self.assertAlmostEqual(
            self.converter.kg_to_g(weight_in_kg), expected_g, places=2
        )

    def test_kg_to_oz(self):
        """Test conversion from kilograms to ounces."""
        weight_in_kg = 1.0
        expected_oz = 35.27
        self.assertAlmostEqual(
            self.converter.kg_to_oz(weight_in_kg), expected_oz, places=2
        )

    def test_lb_to_kg(self):
        """Test conversion from pounds to kilograms."""
        weight_in_lb = 1.0
        expected_kg = 0.45
        self.assertAlmostEqual(
            self.converter.lb_to_kg(weight_in_lb), expected_kg, places=2
        )

    def test_lb_to_g(self):
        """Test conversion from pounds to grams."""
        weight_in_lb = 1.0
        expected_g = 453.59
        self.assertAlmostEqual(
            self.converter.lb_to_g(weight_in_lb), expected_g, places=2
        )

    def test_lb_to_oz(self):
        """Test conversion from pounds to ounces."""
        weight_in_lb = 1.0
        expected_oz = 16.00
        self.assertAlmostEqual(
            self.converter.lb_to_oz(weight_in_lb), expected_oz, places=2
        )

    def test_g_to_kg(self):
        """Test conversion from grams to kilograms."""
        weight_in_g = 1000.0
        expected_kg = 1.00
        self.assertAlmostEqual(
            self.converter.g_to_kg(weight_in_g), expected_kg, places=2
        )

    def test_g_to_lb(self):
        """Test conversion from grams to pounds."""
        weight_in_g = 453.59
        expected_lb = 1.00
        self.assertAlmostEqual(
            self.converter.g_to_lb(weight_in_g), expected_lb, places=2
        )

    def test_g_to_oz(self):
        """Test conversion from grams to ounces."""
        weight_in_g = 28.35
        expected_oz = 1.00
        self.assertAlmostEqual(
            self.converter.g_to_oz(weight_in_g), expected_oz, places=2
        )

    def test_oz_to_kg(self):
        """Test conversion from ounces to kilograms."""
        weight_in_oz = 35.27
        expected_kg = 1.00
        self.assertAlmostEqual(
            self.converter.oz_to_kg(weight_in_oz), expected_kg, places=2
        )

    def test_oz_to_lb(self):
        """Test conversion from ounces to pounds."""
        weight_in_oz = 16.0
        expected_lb = 1.00
        self.assertAlmostEqual(
            self.converter.oz_to_lb(weight_in_oz), expected_lb, places=2
        )

    def test_oz_to_g(self):
        """Test conversion from ounces to grams."""
        weight_in_oz = 1.0
        expected_g = 28.35
        self.assertAlmostEqual(
            self.converter.oz_to_g(weight_in_oz), expected_g, places=2
        )


if __name__ == '__main__':
    unittest.main()
