"""
Distance Unit Test.

Spyder Editor.

Created on Wed Oct 30 21:22:20 2024
@author: BRICE NELSON
"""
import unittest
from distance import Distance


class TestDistanceConversions(unittest.TestCase):
    """Unit tests for the Distance class conversion methods."""

    def setUp(self):
        """Initialize the Distance object for testing."""
        self.converter = Distance()

    # Testing Kilometer Conversions

    def test_km_to_mi(self):
        """Test conversion from kilometers to miles."""
        self.assertAlmostEqual(self.converter.km_mi_conversion(1), 0.621371,
                               places=5)

    def test_km_to_m(self):
        """Test conversion from kilometers to meters."""
        self.assertEqual(self.converter.km_m_conversion(1), 1000)

    def test_km_to_cm(self):
        """Test conversion from kilometers to centimeters."""
        self.assertEqual(self.converter.km_cm_conversion(1), 100000)

    def test_km_to_mm(self):
        """Test conversion from kilometers to millimeters."""
        self.assertEqual(self.converter.km_mm_conversion(1), 1000000)

    def test_km_to_ft(self):
        """Test conversion from kilometers to feet."""
        self.assertAlmostEqual(self.converter.km_ft_conversion(1), 3280.84,
                               places=2)

    def test_km_to_yds(self):
        """Test conversion from kilometers to yards."""
        self.assertAlmostEqual(self.converter.km_yds_conversion(1), 1093.61,
                               places=2)

    def test_km_to_inches(self):
        """Test conversion from kilometers to inches."""
        self.assertAlmostEqual(self.converter.km_inches_conversion(1),
                               39370.1, places=1)

    # Testing Mile Conversions

    def test_mi_to_km(self):
        """Test conversion from miles to kilometers."""
        self.assertAlmostEqual(self.converter.mi_km_conversion(1), 1.60934,
                               places=5)

    def test_mi_to_m(self):
        """Test conversion from miles to meters."""
        self.assertAlmostEqual(self.converter.mi_m_conversion(1), 1609.34,
                               places=2)

    def test_mi_to_cm(self):
        """Test conversion from miles to centimeters."""
        self.assertAlmostEqual(self.converter.mi_cm_conversion(1), 160934,
                               places=0)

    def test_mi_to_mm(self):
        """Test conversion from miles to millimeters."""
        self.assertAlmostEqual(self.converter.mi_mm_conversion(1), 1609344,
                               places=0)

    def test_mi_to_ft(self):
        """Test conversion from miles to feet."""
        self.assertEqual(self.converter.mi_ft_conversion(1), 5280)

    def test_mi_to_yds(self):
        """Test conversion from miles to yards."""
        self.assertEqual(self.converter.mi_yds_conversion(1), 1760)

    def test_mi_to_inches(self):
        """Test conversion from miles to inches."""
        self.assertEqual(self.converter.mi_inches_conversion(1), 63360)

    # Testing Meter Conversions

    def test_m_to_km(self):
        """Test conversion from meters to kilometers."""
        self.assertEqual(self.converter.m_km_conversion(1000), 1)

    def test_m_to_mi(self):
        """Test conversion from meters to miles."""
        self.assertAlmostEqual(self.converter.m_mi_conversion(1609.34), 1,
                               places=2)

    def test_m_to_cm(self):
        """Test conversion from meters to centimeters."""
        self.assertEqual(self.converter.m_cm_conversion(1), 100)

    def test_m_to_mm(self):
        """Test conversion from meters to millimeters."""
        self.assertEqual(self.converter.m_mm_conversion(1), 1000)

    def test_m_to_ft(self):
        """Test conversion from meters to feet."""
        self.assertAlmostEqual(self.converter.m_ft_conversion(1), 3.28084,
                               places=5)

    def test_m_to_yds(self):
        """Test conversion from meters to yards."""
        self.assertAlmostEqual(self.converter.m_yds_conversion(1), 1.09361,
                               places=5)

    def test_m_to_inches(self):
        """Test conversion from meters to inches."""
        self.assertAlmostEqual(self.converter.m_inches_conversion(1), 39.3701,
                               places=4)

    # Testing Centimeter Conversions

    def test_cm_to_km(self):
        """Test conversion from centimeters to kilometers."""
        self.assertAlmostEqual(self.converter.cm_km_conversion(100000), 1,
                               places=5)

    def test_cm_to_mi(self):
        """Test conversion from centimeters to miles."""
        self.assertAlmostEqual(self.converter.cm_mi_conversion(160934), 1,
                               places=0)

    def test_cm_to_m(self):
        """Test conversion from centimeters to meters."""
        self.assertEqual(self.converter.cm_m_conversion(100), 1)

    def test_cm_to_mm(self):
        """Test conversion from centimeters to millimeters."""
        self.assertEqual(self.converter.cm_mm_conversion(1), 10)

    def test_cm_to_ft(self):
        """Test conversion from centimeters to feet."""
        self.assertAlmostEqual(self.converter.cm_ft_conversion(30.48), 1,
                               places=2)

    def test_cm_to_yds(self):
        """Test conversion from centimeters to yards."""
        self.assertAlmostEqual(self.converter.cm_yds_conversion(91.44), 1,
                               places=2)

    def test_cm_to_inches(self):
        """Test conversion from centimeters to inches."""
        self.assertAlmostEqual(self.converter.cm_inches_conversion(2.54), 1,
                               places=2)

    # Testing Millimeter Conversions

    def test_mm_to_km(self):
        """Test conversion from millimeters to kilometers."""
        self.assertAlmostEqual(self.converter.mm_km_conversion(1000000), 1,
                               places=5)

    def test_mm_to_mi(self):
        """Test conversion from millimeters to miles."""
        self.assertAlmostEqual(self.converter.mm_mi_conversion(1609344), 1,
                               places=0)

    def test_mm_to_m(self):
        """Test conversion from millimeters to meters."""
        self.assertEqual(self.converter.mm_m_conversion(1000), 1)

    def test_mm_to_cm(self):
        """Test conversion from millimeters to centimeters."""
        self.assertEqual(self.converter.mm_cm_conversion(10), 1)

    def test_mm_to_ft(self):
        """Test conversion from millimeters to feet."""
        self.assertAlmostEqual(self.converter.mm_ft_conversion(304.8), 1,
                               places=2)

    def test_mm_to_yds(self):
        """Test conversion from millimeters to yards."""
        self.assertAlmostEqual(self.converter.mm_yds_conversion(914.4), 1,
                               places=2)

    def test_mm_to_inches(self):
        """Test conversion from millimeters to inches."""
        self.assertAlmostEqual(self.converter.mm_inches_conversion(25.4), 1,
                               places=2)

    # Testing Foot Conversions

    def test_ft_to_km(self):
        """Test conversion from feet to kilometers."""
        self.assertAlmostEqual(self.converter.ft_km_conversion(3280.84), 1,
                               places=2)

    def test_ft_to_mi(self):
        """Test conversion from feet to miles."""
        self.assertEqual(self.converter.ft_mi_conversion(5280), 1)

    def test_ft_to_cm(self):
        """Test conversion from feet to centimeters."""
        self.assertAlmostEqual(self.converter.ft_cm_conversion(1), 30.48,
                               places=2)

    def test_ft_to_mm(self):
        """Test conversion from feet to millimeters."""
        self.assertAlmostEqual(self.converter.ft_mm_conversion(1), 304.8,
                               places=1)

    def test_ft_to_m(self):
        """Test conversion from feet to meters."""
        self.assertAlmostEqual(self.converter.ft_m_conversion(1), 0.3048,
                               places=4)

    def test_ft_to_yds(self):
        """Test conversion from feet to yards."""
        self.assertEqual(self.converter.ft_yds_conversion(3), 1)

    def test_ft_to_inches(self):
        """Test conversion from feet to inches."""
        self.assertEqual(self.converter.ft_inches_conversion(1), 12)

    # Testing Yard Conversions

    def test_yds_to_km(self):
        """Test conversion from yards to kilometers."""
        self.assertAlmostEqual(self.converter.yds_km_conversion(1093.61), 1,
                               places=2)

    def test_yds_to_mi(self):
        """Test conversion from yards to miles."""
        self.assertEqual(self.converter.yds_mi_conversion(1760), 1)

    def test_yds_to_m(self):
        """Test conversion from yards to meters."""
        self.assertAlmostEqual(self.converter.yds_m_conversion(1), 0.9144,
                               places=4)

    def test_yds_to_cm(self):
        """Test conversion from yards to centimeters."""
        self.assertAlmostEqual(self.converter.yds_cm_conversion(1), 91.44,
                               places=2)

    def test_yds_to_mm(self):
        """Test conversion from yards to millimeters."""
        self.assertAlmostEqual(self.converter.yds_mm_conversion(1), 914.4,
                               places=1)

    def test_yds_to_ft(self):
        """Test conversion from yards to feet."""
        self.assertEqual(self.converter.yds_ft_conversion(1), 3)

    def test_yds_to_inches(self):
        """Test conversion from yards to inches."""
        self.assertEqual(self.converter.yds_inches_conversion(1), 36)

    # Testing Inch Conversions

    def test_inches_to_km(self):
        """Test conversion from inches to kilometers."""
        self.assertAlmostEqual(self.converter.inches_km_conversion(39370.1), 1,
                               places=1)

    def test_inches_to_mi(self):
        """Test conversion from inches to miles."""
        self.assertEqual(self.converter.inches_mi_conversion(63360), 1)

    def test_inches_to_m(self):
        """Test conversion from inches to meters."""
        self.assertAlmostEqual(self.converter.inches_m_conversion(1), 0.0254,
                               places=4)

    def test_inches_to_cm(self):
        """Test conversion from inches to centimeters."""
        self.assertAlmostEqual(self.converter.inches_cm_conversion(1), 2.54,
                               places=2)

    def test_inches_to_mm(self):
        """Test conversion from inches to millimeters."""
        self.assertAlmostEqual(self.converter.inches_mm_conversion(1), 25.4,
                               places=1)

    def test_inches_to_ft(self):
        """Test conversion from inches to feet."""
        self.assertEqual(self.converter.inches_ft_conversion(12), 1)

    def test_inches_to_yds(self):
        """Test conversion from inches to yards."""
        self.assertEqual(self.converter.inches_yds_conversion(36), 1)


# To run the tests
if __name__ == '__main__':
    unittest.main()
