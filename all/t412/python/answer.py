def format_text(input_file='input.txt', output_file='output.txt'):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as f:
            # Read the content of the input file line by line
            lines = f.readlines()

        # Process each line
        processed_lines = []
        for line in lines:
            # Remove newline characters and add a space
            processed_line = line.rstrip('\n')
            processed_lines.append(processed_line)  # Append the processed line

        # Join the processed lines with spaces
        content_without_newlines = ' '.join(processed_lines)

        # Open the output file in write mode
        with open(output_file, 'w') as f:
            # Write the content without newlines to the output file
            f.write(content_without_newlines)

        print("Line breaks removed and spaces added. Output written to", output_file)

    except FileNotFoundError:
        print("Input file not found.")