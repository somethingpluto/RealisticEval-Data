def read_columns(file_name):
    "Entirely written by ChatGPT."
    # Open the file for reading
    with open(file_name) as f:
        # Find the index of the last line that contains the "/" character
        last_slash_index = None
        for i, line in enumerate(f):
            if "/" in line:
                last_slash_index = i

        # If no "/" character was found, raise an error
        if last_slash_index is None:
            raise ValueError("File does not contain '/' character")

        # Read the remaining lines in the file, starting from the last "/"
        f.seek(0)
        lines = f.readlines()[last_slash_index+1:]

        # Remove any empty lines or comments
        lines = [line for line in lines if line.strip() and not line.strip().startswith('!')]

        # Get the row and column count by counting the number of columns in the first line
        col_count = len(lines[0].split())

        # Create an empty numpy array of the required size
        arr = np.zeros((len(lines), col_count))

        # Loop through the lines in the file
        for i, line in enumerate(lines):
            # Split the line into numbers and convert them to floats
            nums = [float(x) for x in line.split()]
            # Store the numbers in the array
            arr[i, :] = nums

    # Return the array
    return arr
