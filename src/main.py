"""Demonstrate the calculator's arithmetic operations."""

from issi_wzio_lab2 import Calculator

if __name__ == '__main__':
    c = Calculator(2.0, 4.0)
    print(c.sum())
    print(c.subtract())
    print(c.multiply())
    print(c.divide())
