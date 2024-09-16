import difflib


def compare_files(file1_path, file2_path):
    # Created by ChatGPT
    with open(file1_path) as file1, open(file2_path) as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()

    diff = difflib.unified_diff(lines1, lines2, fromfile=file1_path, tofile=file2_path)

    for line in diff:
        print(line, end="")