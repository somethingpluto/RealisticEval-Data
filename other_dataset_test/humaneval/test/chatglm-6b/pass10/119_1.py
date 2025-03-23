def check(candidate):

    # Check some simple cases
    assert candidate(['()(', ')']) == 'Yes'
    assert candidate([')', ')']) == 'No'
    assert candidate(['(()(())', '())())']) == 'No'
    assert candidate([')())', '(()()(']) == 'Yes'
    assert candidate(['(())))', '(()())((']) == 'Yes'
    assert candidate(['()', '())']) == 'No'
    assert candidate(['(()(', '()))()']) == 'Yes'
    assert candidate(['((((', '((())']) == 'No'
    assert candidate([')(()', '(()(']) == 'No'
    assert candidate([')(', ')(']) == 'No'
    

    # Check some edge cases that are easy to work out by hand.
    assert candidate(['(', ')']) == 'Yes'
    assert candidate([')', '(']) == 'Yes' 


string1 = '(())()'
string2 = '()'

# Check if the strings are balanced
if not match_parens(string1+string2):
    print("The strings are not balanced.")
    return "No"

# Check if it is possible to concatenate the strings in some order
if match_parens(string1+'('+string2):
    print("Yes, it is possible to concatenate the strings in some order.")
    return "Yes"

candidate = match_parens
check(candidate)