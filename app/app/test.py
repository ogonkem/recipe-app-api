"""
Sample tests
"""
from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the Calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 7)

        self.assertEqual(res, 12)

    def test_subtract_numbers(self):
        """Test adding numbers together."""
        res = calc.subtract(7, 4)

        self.assertEqual(res, 3)