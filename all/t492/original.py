def save_content_to_file(content, path):
    # remove redundant whitespace
    content = '\n'.join(line for line in content.splitlines() if line.strip())
    while "  " in content:
        content = content.replace("  ", " ")
    content = '\n'.join(line.strip() for line in content.splitlines())

    with open(path, 'w', encoding='utf-8') as file:
        file.write(content)