"""
Temperature Unit Test.

Spyder Editor.

Created on Wed Oct 30 22:42:05 2024
@author: BRICE NELSON
"""
import unittest
from temperature import Temperature


class TestTemperatureConversions(unittest.TestCase):
    """
    Unit tests for the Temperature class conversion methods.
    """

    def setUp(self):
        """Initialize the Temperature object for testing."""
        self.converter = Temperature()

    # *************** Testing Celsius Conversions ***************

    def test_celsius_to_fahrenheit(self):
        """Test conversion from Celsius to Fahrenheit."""
        self.assertAlmostEqual(self.converter.c_f_conversion(0), 32.0,
                               places=2)
        self.assertAlmostEqual(self.converter.c_f_conversion(100), 212.0,
                               places=2)

    def test_celsius_to_kelvin(self):
        """Test conversion from Celsius to Kelvin."""
        self.assertAlmostEqual(self.converter.c_k_conversion(0), 273.15,
                               places=2)
        self.assertAlmostEqual(self.converter.c_k_conversion(-273.15), 0,
                               places=2)

    def test_celsius_to_celsius(self):
        """Test conversion from Celsius to Celsius."""
        self.assertEqual(self.converter.c_c_conversion(25), 25)
        self.assertEqual(self.converter.c_c_conversion(-10), -10)

    # *************** Testing Fahrenheit Conversions ***************

    def test_fahrenheit_to_celsius(self):
        """Test conversion from Fahrenheit to Celsius."""
        self.assertAlmostEqual(self.converter.f_c_conversion(32), 0.0,
                               places=2)
        self.assertAlmostEqual(self.converter.f_c_conversion(212), 100.0,
                               places=2)

    def test_fahrenheit_to_kelvin(self):
        """Test conversion from Fahrenheit to Kelvin."""
        self.assertAlmostEqual(self.converter.f_k_conversion(32), 273.15,
                               places=2)
        self.assertAlmostEqual(self.converter.f_k_conversion(-459.67), 0,
                               places=2)

    def test_fahrenheit_to_fahrenheit(self):
        """Test conversion from Fahrenheit to Fahrenheit."""
        self.assertEqual(self.converter.f_f_conversion(50), 50)
        self.assertEqual(self.converter.f_f_conversion(-10), -10)

    # *************** Testing Kelvin Conversions ***************

    def test_kelvin_to_celsius(self):
        """Test conversion from Kelvin to Celsius."""
        self.assertAlmostEqual(self.converter.k_c_conversion(273.15), 0,
                               places=2)
        self.assertAlmostEqual(self.converter.k_c_conversion(0), -273.15,
                               places=2)

    def test_kelvin_to_fahrenheit(self):
        """Test conversion from Kelvin to Fahrenheit."""
        self.assertAlmostEqual(self.converter.k_f_conversion(273.15), 32,
                               places=2)
        self.assertAlmostEqual(self.converter.k_f_conversion(0), -459.67,
                               places=2)

    def test_kelvin_to_kelvin(self):
        """Test conversion from Kelvin to Kelvin."""
        self.assertEqual(self.converter.k_k_conversion(100), 100)
        self.assertEqual(self.converter.k_k_conversion(273.15), 273.15)


# To run the tests
if __name__ == '__main__':
    unittest.main()
