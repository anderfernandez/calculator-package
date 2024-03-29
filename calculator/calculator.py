class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    """

    def add(self, a: float, b: float) -> float:
        """
        Adds two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The sum of the two numbers.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Subtracts two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The difference between the two numbers.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Multiplies two numbers.

        Args:
            a (float): The first number.
            b (float): The second number.

        Returns:
            float: The product of the two numbers.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Divides two numbers.

        Args:
            a (float): The dividend.
            b (float): The divisor.

        Returns:
            float: The quotient of the two numbers.
        """
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b