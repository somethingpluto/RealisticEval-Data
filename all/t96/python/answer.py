def changed_clef(abc: str, clef: str = "bass") -> str:
    # Find the index of the key signature line
    clef_index = abc.find("\nK:")

    # If the key signature is found
    if clef_index != -1:
        # Find the next newline character after the key signature line,
        # or if none exists, use the end of the string
        next_newline = abc.find("\n", clef_index + 1)
        if next_newline == -1:
            next_newline = len(abc)

        # Create the string to inject, which includes the clef
        injection = f" clef={clef}"

        # Construct the new ABC string with the injected clef
        return f"{abc[:next_newline]}{injection}{abc[next_newline:]}"

    # If the key signature is not found, return the original string
    return abc