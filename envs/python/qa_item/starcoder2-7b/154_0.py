import re
from typing import List

def parse_git_diff(diff_text: str) -> List[dict]:
    # Split the diff text into individual file diffs
    file_diffs = re.split(r'diff --git a/(.+) b/(.+)\n', diff_text)[1:]

    result = []
    for file_diff in file_diffs:
        # Split the file diff into header and body
        header, body = file_diff.split('\n', 1)

        # Extract the file name
        file_name = re.search(r'a/(.+) b/(.+)', header).group(1)

        # Initialize counters for added and removed lines
        added_lines = 0
        removed_lines = 0

        # Iterate over the body of the file diff
        for line in body.split('\n'):
            if line.startswith('+'):
                added_lines += 1
            elif line.startswith('-'):
                removed_lines += 1

        # Append the file diff details to the result
        result.append({
            'file_name': file_name,
            'added_lines': added_lines,
            'removed_lines': removed_lines
        })

    return result
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