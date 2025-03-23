def check(candidate):

    # Check some simple cases
    assert candidate(['**', '*', '+'], [2, 3, 4, 5]) == 37
    assert candidate(['+', '*', '-'], [2, 3, 4, 5]) == 9
    assert candidate(['//', '*'], [7, 3, 4]) == 8, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

def do_algebra(operator, operand):
    if not operator or not operand:
        return None

    if len(operator)!= len(operand) - 1:
        raise ValueError("The length of operator list should be equal to the length of operand list minus one.")

    if len(operator) == 1:
        return operand[0] * operator[0] if operator[0] == '*' else operand[0] if operator[0] == '+' else -operand[0] if operator[0] == '-' else operand[0] ** operand[0]

    result = operand[0]
    for i in range(1, len(operand)):
        operation = operator[i - 1]
        right_operand = operand[i]
        if operation == '+':
            result += right_operand
        elif operation == '-':
            result -= right_operand
        elif operation == '*':
            result *= right_operand
        elif operation == '//':
            result //= right_operand
        elif operation == '**':
            result **= right_operand

    return result
candidate = do_algebra
check(candidate)