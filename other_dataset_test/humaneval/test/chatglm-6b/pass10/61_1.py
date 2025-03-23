

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


 bracketings = "()"
correct_bracketing_result = correct_bracketing( bracketings)
print(correct_bracketing_result) # True
python
 bracketings = ")(()"
correct_bracketing_result = correct_bracketing( bracketings)
print(correct_bracketing_result) # False

candidate = correct_bracketing
check(candidate)