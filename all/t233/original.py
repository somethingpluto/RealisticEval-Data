def remove_comments(string: str):
    isInComment=False
    returnVal = ""
    for char in string:
        if char == '#':
            isInComment = True
        elif char == "\n":
            isInComment = False
        if not isInComment:
            returnVal += char
    return returnVal