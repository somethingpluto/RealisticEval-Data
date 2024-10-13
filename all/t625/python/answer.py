def read_data_from_file(path: str):
    data_list = []
    try:
        with open(path, 'r') as reader:
            for line in reader:
                # Trim leading and trailing whitespace
                line = line.strip()

                # Try to parse as an integer
                try:
                    int_value = int(line)
                    data_list.append(int_value)
                    continue  # Go to the next line
                except ValueError:
                    # Not an integer, continue to check for float
                    pass

                # Try to parse as a floating-point number
                try:
                    float_value = float(line)
                    data_list.append(float_value)
                    continue  # Go to the next line
                except ValueError:
                    # Not a float, continue to check for string
                    pass

                # If it's not an integer or float, it's treated as a string
                data_list.append(line)
    except IOError as e:
        print(e)
        raise ValueError(f"Error reading file: {e}")

    return data_list