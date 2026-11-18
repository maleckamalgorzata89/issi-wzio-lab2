"""Module providing a simple calculator."""
class Calculator:
    """Perform basic arithmetic operations on two numbers"""
    def __init__(self,op1:float,op2:float) -> None:
        self.__op1 = op1
        self.__op2 = op2

    def sum(self) -> float:
        """Return the sum of the two numbers"""
        return self.__op1 + self.__op2

    def subtract(self) -> float:
        """Return the subtraction of the two numbers"""
        return self.__op1 - self.__op2

    def multiply(self) -> float:
        """Return the multiplication of the two numbers"""
        return self.__op1 * self.__op2

    def divide(self) -> float:
        """Return the division of the two numbers"""
        if self.__op2==0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return self.__op1 / self.__op2
