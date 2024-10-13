def perform_operation(a: float, b: float, op: str) -> float:
    """Performs a mathematical operation on two operands.

    This function takes two float values and an operator character, and performs
    the specified arithmetic operation. Supported operations include addition,
    subtraction, multiplication, division, and exponentiation.

    Args:
        a (float): The first operand.
        b (float): The second operand.
        op (str): A character representing the operation to perform:
                  '+' for addition,
                  '-' for subtraction,
                  '*' for multiplication,
                  '/' for division,
                  '^' for exponentiation.

    Returns:
        float: The result of the operation.

    Raises:
        ValueError: If the operator is not recognized or if
                    there is an attempt to divide by zero.
    """
