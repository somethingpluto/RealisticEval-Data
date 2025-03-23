

METADATA = {}


def check(candidate):
    assert candidate("()")
    assert candidate("(()())")
    assert candidate("()()(()())()")
    assert candidate("()()((()()())())(()()(()))")
    assert not candidate("((()())))")
    assert not candidate(")(()")
    assert not candidate("(")
    assert not candidate("((((")
    assert not candidate(")")
    assert not candidate("(()")
    assert not candidate("()()(()())())(()")
    assert not candidate("()()(()())()))()")

def correct_bracketing(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack or stack.pop()!= '(':
                return False
    return not stack  # returns True if the stack is empty

# Test cases
print(correct_bracketing("("))  # False
print(correct_bracketing("()"))  # True
print(correct_bracketing("(()())"))  # True
print(correct_bracketing(")(()"))  # False
candidate = correct_bracketing
check(candidate)