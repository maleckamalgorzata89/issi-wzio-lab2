"""Test the calculator's arithmetic operations."""

import pytest
from issi_wzio_lab2.calculator import Calculator


class TestCalculator:
    """Cover calculator operations and edge cases."""

    def test_sum(self):
        """Check addition of positive numbers."""
        c = Calculator(4.0, 2.0)
        assert c.sum() == 6.0

    def test_sum_negative_numbers(self):
        """Check addition of negative numbers."""
        c = Calculator(-4.0, -2.0)
        assert c.sum() == -6.0

    def test_sum_large_numbers(self):
        """Check addition of large numbers."""
        c = Calculator(1e100, 2e100)
        assert pytest.approx(c.sum()) == 3e100

    def test_subtract(self):
        """Check subtraction of positive numbers."""
        c = Calculator(4.0, 2.0)
        assert c.subtract() == 2.0

    def test_subtract_negative_numbers(self):
        """Check subtraction of negative numbers."""
        c = Calculator(-4.0, -2.0)
        assert c.subtract() == -2.0

    def test_subtract_resulting_in_zero(self):
        """Check that subtracting equal numbers gives zero."""
        c = Calculator(4.0, 4.0)
        assert c.subtract() == 0.0

    def test_multiply(self):
        """Check multiplication of positive numbers."""
        c = Calculator(4.0, 2.0)
        assert c.multiply() == 8.0

    def test_multiply_negative_numbers(self):
        """Check that multiplying two negative numbers gives a positive result."""
        c = Calculator(-4.0, -2.0)
        assert c.multiply() == 8.0

    def test_multiply_large_numbers(self):
        """Check multiplication with a large operand."""
        c = Calculator(1e100, 2.0)
        assert pytest.approx(c.multiply()) == 2e100

    def test_multiply_overflow(self):
        """Check that multiplication overflow produces infinity."""
        c = Calculator(1e308, 1e308)
        result = c.multiply()
        assert result == float("inf")

    def test_divide(self):
        """Check division of positive numbers."""
        c = Calculator(4.0, 2.0)
        assert c.divide() == 2.0

    def test_divide_negative_numbers(self):
        """Check that dividing two negative numbers gives a positive result."""
        c = Calculator(-4.0, -2.0)
        assert c.divide() == 2.0

    def test_divide_by_zero(self):
        """Check that division by zero raises ZeroDivisionError."""
        c = Calculator(4.0, 0.0)
        with pytest.raises(ZeroDivisionError):
            c.divide()

    def test_divide_repeating_decimal(self):
        """Check division with a repeating decimal result."""
        c = Calculator(1.0, 3.0)
        assert c.divide() == pytest.approx(0.3333333333, abs=1e-9)

    @pytest.mark.parametrize("a, b, expected", [
        (2, 3, 5),
        (-1, -2, -3),
        (2.5, 3.5, 6.0),
    ])
    def test_add_parametrized(self, a, b, expected):
        """Check addition"""
        calc = Calculator(a, b)
        assert calc.sum() == expected
