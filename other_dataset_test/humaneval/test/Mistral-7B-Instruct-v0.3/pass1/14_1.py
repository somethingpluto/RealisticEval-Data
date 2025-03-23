

METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def check(candidate):
    assert candidate('') == []
    assert candidate('asdfgh') == ['a', 'as', 'asd', 'asdf', 'asdfg', 'asdfgh']
    assert candidate('WWW') == ['W', 'WW', 'WWW']
def all_prefixes(string: str) -> List[str]:
    prefixes = []
    for i in range(len(string) + 1):
        prefix = string[:i]
        prefixes.append(prefix)
    return prefixes
candidate = all_prefixes
check(candidate)