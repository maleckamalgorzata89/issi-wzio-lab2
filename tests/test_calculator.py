import pytest
from issi_wzio_lab2.calculator import Calculator


class TestCalculator:
    def test_sum(self):
        c = Calculator(4.0, 2.0)
        assert c.sum() == 6.0

    def test_sum_negative_numbers(self):
        c = Calculator(-4.0, -2.0)
        assert c.sum() == -6.0

    def test_sum_large_numbers(self):
        c = Calculator(1e100, 2e100)
        assert pytest.approx(c.sum()) == 3e100

    def test_subtract(self):
        c = Calculator(4.0, 2.0)
        assert c.subtract() == 2.0

    def test_subtract_negative_numbers(self):
        c = Calculator(-4.0, -2.0)
        assert c.subtract() == -2.0

    def test_subtract_resulting_in_zero(self):
        c = Calculator(4.0, 4.0)
        assert c.subtract() == 0.0

    def test_multiply(self):
        c = Calculator(4.0, 2.0)
        assert c.multiply() == 8.0

    def test_multiply_negative_numbers(self):
        c = Calculator(-4.0, -2.0)
        assert c.multiply() == 8.0

    def test_multiply_large_numbers(self):
        c = Calculator(1e100, 2.0)
        assert pytest.approx(c.multiply()) == 2e100

    def test_multiply_overflow(self):
        c = Calculator(1e308, 1e308)
        result = c.multiply()
        assert result == float("inf")

    def test_divide(self):
        c = Calculator(4.0, 2.0)
        assert c.divide() == 2.0

    def test_divide_negative_numbers(self):
        c = Calculator(-4.0, -2.0)
        assert c.divide() == 2.0

    def test_divide_by_zero(self):
        c = Calculator(4.0, 0.0)
        with pytest.raises(ZeroDivisionError):
            c.divide()

    def test_divide_repeating_decimal(self):
        c = Calculator(1.0, 3.0)
        assert c.divide() == pytest.approx(0.3333333333, abs=1e-9)
