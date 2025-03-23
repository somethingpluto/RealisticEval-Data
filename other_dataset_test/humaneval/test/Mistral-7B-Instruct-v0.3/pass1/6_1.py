

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('(()()) ((())) () ((())()())') == [2, 3, 1, 3]
    assert candidate('() (()) ((())) (((())))') == [1, 2, 3, 4]
    assert candidate('(()(())((())))') == [4]
def parse_nested_parens(paren_string: str) -> List[int]:
    def count_nesting(s: str) -> int:
        count = 0
        for c in s:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return count

    return [count_nesting(p) for p in paren_string.split() if p]
candidate = parse_nested_parens
check(candidate)