import re

def transform_text(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()
    except IOError as e:
        print(f"Error reading from file {input_file}: {e}")
        return

    transformed_content = transform_parentheses(content)

    try:
        with open(output_file, 'w') as file:
            file.write(transformed_content)
    except IOError as e:
        print(f"Error writing to file {output_file}: {e}")

def transform_parentheses(text):
    pattern = re.compile(r'\(\*(.*?)\*\)')

    def replace(match):
        inner_content = match.group(1)
        inner_content = inner_content.replace('*', '')
        return f'(*{inner_content}*)'

    transformed_text = pattern.sub(replace, text)
    return transformed_text

# Example usage
input_file_path = '_build/markdown/metaphor_python.md'  # replace with your input file path
output_file_path = '_build/markdown/metaphor_python.md'  # replace with your output file path

transform_text(input_file_path, output_file_path)
