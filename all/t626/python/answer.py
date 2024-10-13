def read_file_and_process_lines(self, path):

    processed_lines = []
    try:
        with open(path, 'r') as file:
            for line in file:
                # Remove inline comments
                line = line.split('#')[0].strip()
                # Only add non-empty lines to the list
                if line:
                    processed_lines.append(line)
    except IOError as e:
        print(f"Error reading file: {e}")
        raise ValueError(f"Error reading file: {e}")

    return processed_lines