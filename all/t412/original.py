# This script is for formatting text from PDFs which often gets
# split up into multiple lines. Generated by chatgpt
#
# Steps:
# Reads input.txt, removes newlines, adds a space
# between each line if there is not one already, and writes the output
# to output.txt.

def remove_newlines(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as f:
            # Read the content of the input file line by line
            lines = f.readlines()

        # Process each line
        processed_lines = []
        for line in lines:
            # Remove newline characters and add a space if there isn't one already
            processed_line = line.rstrip('\n')
            if not processed_line.endswith(' '):
                processed_line += ' '
            processed_lines.append(processed_line)

        # Join the processed lines with spaces
        content_without_newlines = ''.join(processed_lines)

        # remove trailing space
        content_without_newlines = content_without_newlines[:-1]

        # Open the output file in write mode
        with open(output_file, 'w') as f:
            # Write the content without newlines to the output file
            f.write(content_without_newlines)

        print("Newlines removed successfully. Output written to", output_file)

    except FileNotFoundError:
        print("Input file not found.")


# Usage: Pass input and output file paths as arguments
remove_newlines("input.txt", "output.txt")