class Calculator:
    def add(self, a: float, b: float) -> float:
        """
        Returns the sum of a and b.
        """
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """
        Returns the difference of a and b.
        """
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """
        Returns the product of a and b.
        """
        return a * b

    def divide(self, a: float, b: float) -> float:
        """
        Returns the quotient of a and b.
        Raises ValueError if b is zero.
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b