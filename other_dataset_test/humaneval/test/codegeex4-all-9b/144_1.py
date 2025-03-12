def check(candidate):

    # Check some simple cases
    assert candidate("example.txt") == 'Yes'
    assert candidate("1example.dll") == 'No'
    assert candidate('s1sdf3.asd') == 'No'
    assert candidate('K.dll') == 'Yes'
    assert candidate('MY16FILE3.exe') == 'Yes'
    assert candidate('His12FILE94.exe') == 'No'
    assert candidate('_Y.txt') == 'No'
    assert candidate('?aREYA.exe') == 'No'
    assert candidate('/this_is_valid.dll') == 'No'
    assert candidate('this_is_valid.wow') == 'No'
    assert candidate('this_is_valid.txt') == 'Yes'
    assert candidate('this_is_valid.txtexe') == 'No'
    assert candidate('#this2_i4s_5valid.ten') == 'No'
    assert candidate('@this1_is6_valid.exe') == 'No'
    assert candidate('this_is_12valid.6exe4.txt') == 'No'
    assert candidate('all.exe.txt') == 'No'
    assert candidate('I563_No.exe') == 'Yes'
    assert candidate('Is3youfault.txt') == 'Yes'
    assert candidate('no_one#knows.dll') == 'Yes'
    assert candidate('1I563_Yes3.exe') == 'No'
    assert candidate('I563_Yes3.txtt') == 'No'
    assert candidate('final..txt') == 'No'
    assert candidate('final132') == 'No'
    assert candidate('_f4indsartal132.') == 'No'
    
        

    # Check some edge cases that are easy to work out by hand.
    assert candidate('.txt') == 'No'
    assert candidate('s.') == 'No'

def file_name_check(file_name):
    """Create a function which takes a string representing a file's name, and returns
    'Yes' if the the file's name is valid, and returns 'No' otherwise.
    A file's name is considered to be valid if and only if all the following conditions 
    are met:
    - There should not be more than three digits ('0'-'9') in the file's name.
    - The file's name contains exactly one dot '.'
    - The substring before the dot should not be empty, and it starts with a letter from 
    the latin alphapet ('a'-'z' and 'A'-'Z').
    - The substring after the dot should be one of these: ['txt', 'exe', 'dll']
    Examples:
    file_name_check("example.txt") # => 'Yes'
    file_name_check("1example.dll") # => 'No' (the name should start with a latin alphapet letter)
    """
    import re
    def is_valid_file_name(file_name):
        # Check for more than three digits
        if sum(c.isdigit() for c in file_name) > 3:
            return 'No'
        # Check for exactly one dot
        if file_name.count('.') != 1:
            return 'No'
        # Split the name into name and extension
        name, extension = file_name.split('.')
        # Check the name starts with a letter
        if not re.match('^[A-Za-z]', name):
            return 'No'
        # Check the extension is valid
        if extension not in ['txt', 'exe', 'dll']:
            return 'No'
        return 'Yes'

    return is_valid_file_name(file_name)
candidate = file_name_check
check(candidate)