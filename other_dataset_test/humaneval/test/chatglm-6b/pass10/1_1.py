

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

>>> separate_paren_groups('( ) (( )) (( )( ))')
['()', '(())', '(()())']

import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if re.match(r'[()]+', paren_string):
        # check if the string is a valid balanced group
        if len(paren_string) > 0 and len(paren_string[0]) == 2:
            # check if the string starts with an open brace
            if re.match(r'^((', paren_string):
                # split the string into a list of groups
                paren_groups = []
                for i in range(len(paren_string)):
                    # check if the next character is a closing parenthesis
                    if re.match(r'(', paren_string[i+1]):
                        # check if the next character is an opening parenthesis
                        if re.match(r'^(', paren_string[i+2]):
                            # add the group to the list
                            paren_groups.append(paren_string[i+1])
                        else:
                            # add the group if it's not a closing parenthesis
                            # if it's not a closing parenthesis, the group is not a valid balanced group
                            # so the function will return an error
                            raise Exception('Invalid balanced group')
                else:
                    # add the opening parenthesis to the list
                    paren_groups.append(paren_string[i])
    else:
        # check if the string is not a valid balanced group
        raise Exception('Invalid balanced group')
    return paren_groups

candidate = separate_paren_groups
check(candidate)