def split_comma(s):
    # Clear the output list to avoid residual data
    vect = []

    # Process each comma-separated token
    for token in s.split(','):
        # Trim leading and trailing whitespace
        token = token.strip()

        # Only add non-empty tokens to the list
        if token:
            vect.append(token)

    return vect
