/**
 * Parsing a string containing the contents of a Git diff returns a vector of objects with details of each file's changes
 *
 * @param diffText - The Git diff text to parse.
 * @returns A vector of objects representing the diff for each file.
 */
std::vector<GitDiffFile> parseGitDiff(const std::string& diffText);