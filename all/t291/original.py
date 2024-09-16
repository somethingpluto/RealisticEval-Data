#
# Written with ChatGPT ..
# https://chat.openai.com/
#
# prompt: create python to read in file and add a string to each line and output to another file
#
def read_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return lines

def write_file(filename, lines):
    with open(filename, 'w') as file:
        file.writelines(lines)

def add_string_to_lines(input_file, output_file, additional_string):
    lines = read_file(input_file)
    modified_lines = [additional_string + line.strip()  + '\n' for line in lines]
    write_file(output_file, modified_lines)
    print("File written successfully!")

# Example usage
input_filename = 'labels.txt'
output_filename = 'labels.list'
additional_string = "__label__"

add_string_to_lines(input_filename, output_filename, additional_string)