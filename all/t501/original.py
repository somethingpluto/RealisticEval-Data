def flags_long2short(long_flags):
    """ Handy function to convert long flags to short flags, e.g. "f1_p1_g1_b1_c1" to "fpgbc".
        Created by ChatGPT GPT-4 model.
    """
    # Split the string by underscores
    parts = long_flags.split('_')
    result = []

    # Iterate over the split parts
    for part in parts:
        # Check if the part has a length of 2 and ends with "1"
        if len(part) == 2 and part[1] == '1':
            # Append the first character of the part to the result
            result.append(part[0])

    # Join the result list to get the final string
    return ''.join(result)