from collections import Counter

def min_window(s: str, t: str) -> str:
    """
    Find the minimum window substring in `s` that contains all characters of `t`.

    Parameters:
    - s: The input string in which to search for the substring.
    - t: The target string whose characters must be included in the substring.

    Returns:
    - The minimum window substring of `s` that contains all characters of `t`.
      Returns an empty string if no such substring exists.
    """
    
    # If the length of s is less than t, return an empty string
    if len(s) < len(t):
        return ''
    
    # Count characters in t
    substring_counter = Counter(t)
    # Counter for the current window
    counter = Counter()
    
    # Initialize pointers and variables for the minimum window
    l = r = 0
    min_length = float('inf')
    min_string = ''

    # Iterate over s using the right pointer
    for r, char in enumerate(s):
        # If the character is in the substring_counter, update the current counter
        if char in substring_counter:
            counter[char] += 1
        
        # Check if the current window contains all characters in t
        while counter & substring_counter == substring_counter:
            # Update the minimum window if a smaller one is found
            if r - l + 1 < min_length:
                min_length = r - l + 1
                min_string = s[l:r + 1]

            # Move the left pointer to try to shrink the window
            left_char = s[l]
            if left_char in substring_counter:
                counter[left_char] -= 1
            l += 1

    # Return the minimum window found or an empty string if none exists
    return min_string if min_length <= len(s) else ''
