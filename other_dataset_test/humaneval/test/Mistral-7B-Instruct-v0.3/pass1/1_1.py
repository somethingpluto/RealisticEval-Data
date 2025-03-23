

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [
        '(()())', '((()))', '()', '((())()())'
    ]
    assert candidate('() (()) ((())) (((())))') == [
        '()', '(())', '((()))', '(((())))'
    ]
    assert candidate('(()(())((())))') == [
        '(()(())((())))'
    ]
    assert candidate('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ Separate nested parentheses groups into separate strings and return the list of those. """

    # Initialize an empty list to store the balanced parentheses groups
    groups = []

    # Initialize an empty stack
    stack = []

    # Iterate through each character in the input string
    for char in paren_string:
        # If we encounter an opening parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)
        # If we encounter a closing parenthesis, pop from the stack and check if the stack is empty
        elif char == ')':
            # If the stack is empty, it means there's a mismatch in parentheses
            if not stack:
                return []
            # Pop the opening parenthesis from the stack and append the current group to the groups list
            group = ''
            while stack and stack[-1]!= '(':
                group += stack.pop()
            stack.pop()
            groups.append(group)

    # If there are any remaining opening parentheses in the stack, it means there's a mismatch in parentheses
    if stack:
        return []

    # Return the list of balanced parentheses groups
    return groups
candidate = separate_paren_groups
check(candidate)