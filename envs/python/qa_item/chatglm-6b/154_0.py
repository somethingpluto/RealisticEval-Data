
from typing import List

def parse_git_diff(diff_text: str) -> List[str]:
    """
    Parses a string containing the contents of a Git diff and returns a list of objects
    detailing the changes for each file.

    Args:
        diff_text (str): The Git diff text to parse.

    Returns:
        List[str]: A list of objects representing the diff for each file, where each object
            contains details about the changes, such as file name, added lines, and removed
            lines.
    """
    # Split the diff text into lines
    diff_lines = diff_text.split("\n")

    # Initialize an empty list to store the objects
    objects = []

    # Iterate over the lines of the diff text
    for line in diff_lines:
        # Check if the line is a file name
        if line.startswith("File :"):
            # Split the line into a file name and a list of lines
            file_name = line[7:].split(" ")[0]
            # Append the file name to the list of objects
            objects.append(file_name)

        # Check if the line contains changes
        if line.startswith("Add") or line.startswith("Remove"):
            # Split the line into a list of changes
            changes = line.split(" ")[1:]
            # Append the changes to the list of objects
            objects.append(changes)

    return objects

import unittest

class TestParseGitDiff(unittest.TestCase):

    def test_parse_simple_file_addition(self):
        diff_text = (
            "diff --git a/file.txt b/file.txt\n"
            "new file mode 100644\n"
            "index 0000000..e69de29\n"
            "--- /dev/null\n"
            "+++ b/file.txt"
        )
        result = parse_git_diff(diff_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].oldPath, 'file.txt')
        self.assertEqual(result[0].newPath, 'file.txt')
        self.assertEqual(result[0].newFileMode, '100644')

    def test_parse_simple_file_deletion(self):
        diff_text = (
            "diff --git a/file.txt b/file.txt\n"
            "deleted file mode 100644\n"
            "index e69de29..0000000\n"
            "--- a/file.txt\n"
            "+++ /dev/null"
        )
        result = parse_git_diff(diff_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].oldPath, 'file.txt')
        self.assertEqual(result[0].newPath, 'file.txt')
        self.assertEqual(result[0].deletedFileMode, '100644')

    def test_parse_file_modification_with_changes(self):
        diff_text = (
            "diff --git a/file.txt b/file.txt\n"
            "index e69de29..d95f3ad 100644\n"
            "--- a/file.txt\n"
            "+++ b/file.txt\n"
            "@@ -0,0 +1 @@\n"
            "+Hello World"
        )
        result = parse_git_diff(diff_text)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].oldPath, 'file.txt')
        self.assertEqual(result[0].newPath, 'file.txt')
        self.assertEqual(result[0].index, 'e69de29..d95f3ad')
        self.assertEqual(result[0].changes, [
            {"code": "--- a/file.txt"},
            {"code": "+++ b/file.txt"},
            {"diff": '@@ -0,0 +1 @@'},
            {"code": '+Hello World'}
        ])

    def test_handle_multiple_file_diffs(self):
        diff_text = (
            "diff --git a/file1.txt b/file1.txt\n"
            "index e69de29..d95f3ad 100644\n"
            "--- a/file1.txt\n"
            "+++ b/file1.txt\n"
            "@@ -0,0 +1 @@\n"
            "+Hello World\n"
            "diff --git a/file2.txt b/file2.txt\n"
            "index 0a1b2c3..d4e5f6a 100644\n"
            "--- a/file2.txt\n"
            "+++ b/file2.txt\n"
            "@@ -1 +1 @@\n"
            "-Hello\n"
            "+Hi"
        )
        result = parse_git_diff(diff_text)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0].oldPath, 'file1.txt')
        self.assertEqual(result[1].oldPath, 'file2.txt')

    def test_return_empty_array_for_empty_diff_text(self):
        result = parse_git_diff('')
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()