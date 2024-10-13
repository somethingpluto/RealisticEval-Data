import math

def apply_op(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ValueError("Division by zero is not allowed.")
        return a / b
    elif op == '^':
        return math.pow(a, b)
    else:
        raise ValueError("Invalid operator.")