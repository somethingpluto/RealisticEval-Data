from typing import List, Optional


class GitDiffChange:
    def __init__(self, diff: Optional[str] = None, code: Optional[str] = None):
        self.diff = diff
        self.code = code

class GitDiffFile:
    def __init__(self, old_path: str, new_path: str):
        self.old_path = old_path
        self.new_path = new_path
        self.changes: List[GitDiffChange] = []
        self.new_file_mode: Optional[str] = None
        self.deleted_file_mode: Optional[str] = None
        self.index: Optional[str] = None

def parse_git_diff(diff_text: str) -> List[GitDiffFile]:
    """
    Parsing a string containing the contents of a Git diff returns an array of objects with details of each file's changes.

    :param diff_text: The Git diff text to parse.
    :return: A list of GitDiffFile objects representing the diff for each file.
    """
    diff_lines = diff_text.split('\n')
    file_diffs: List[GitDiffFile] = []
    current_file: Optional[GitDiffFile] = None

    for line in diff_lines:
        if line.startswith('diff --git a/'):
            # When a new file diff starts, push the current file diff to the array
            if current_file:
                file_diffs.append(current_file)

            # Extract the old and new paths from the diff line
            paths = line.split(' ')[2:]  # Skip the first two elements
            old_path = paths[0][2:]  # Removing 'a/'
            new_path = paths[1][2:]  # Removing 'b/'
            current_file = GitDiffFile(old_path, new_path)

        elif line.startswith('new file mode'):
            if current_file:
                current_file.new_file_mode = line.split(' ')[3]

        elif line.startswith('deleted file mode'):
            if current_file:
                current_file.deleted_file_mode = line.split(' ')[3]

        elif line.startswith('index'):
            if current_file:
                current_file.index = line.split(' ')[1]

        elif line.startswith('@@'):
            # Start of a hunk; add it to the changes array
            if current_file:
                current_file.changes.append(GitDiffChange(diff=line))

        elif current_file and (line.startswith('+') or line.startswith('-') or line.startswith(' ')):
            # Line additions, deletions, or context
            current_file.changes.append(GitDiffChange(code=line))

    # Push the last file diff after the loop ends
    if current_file:
        file_diffs.append(current_file)

    return file_diffs