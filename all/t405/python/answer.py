def remove_parts_of_string(*strings):
    results = []
    for string in strings:
        try:
            # Remove all characters before the first uppercase letter
            index = [i for i in range(len(string)) if string[i].isupper()][0]
            string = string[index:]

            # Remove all characters before the first lowercase letter
            index = [i for i in range(len(string)) if string[i].islower()][0]
            string = string[index - 1:]

            results.append(string)
        except IndexError:
            # Handle cases where no uppercase or lowercase letters are found
            results.append(string)  # You may decide to append an empty string or an error message

    return results