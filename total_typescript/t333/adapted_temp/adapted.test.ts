describe('replaceText', () => {
  // Test: Correct replacement of a GitHub username mention
  test('replaces GitHub username mentions correctly', () => {
    const input = 'This was fixed by @user123';
    const expected = 'This was fixed by [@user123](https://github.com/user123)';
    expect(replaceText(input)).toBe(expected);
  });

  // Test: Correct replacement of a GitHub issue number
  test('replaces GitHub issue numbers correctly', () => {
    const input = 'The bug was reported in #456';
    const expected = 'The bug was reported in [#456](https://github.com/umijs/mako/pull/456)';
    expect(replaceText(input)).toBe(expected);
  });

  // Test: Handles multiple replacements within a single string
  test('handles multiple replacements in a single string', () => {
    const input = 'Fixed by @dev and discussed in #789';
    const expected = 'Fixed by [@dev](https://github.com/dev) and discussed in [#789](https://github.com/umijs/mako/pull/789)';
    expect(replaceText(input)).toBe(expected);
  });

  // Test: Returns the original string if there are no matches
  test('returns original text if no replacements apply', () => {
    const input = 'No mentions or issues here!';
    expect(replaceText(input)).toBe(input);
  });

  // Test: Correctly ignores incorrect formats that should not be replaced
  test('ignores incorrect formats', () => {
    const input = 'Check by@unknown in#1023';
    expect(replaceText(input)).toBe(input);
  });
});
/**
 * Replaces mentions of GitHub usernames and issue numbers in a text string with Markdown links.
 * @param {string} toReplace - The text in which replacements will be made.
 * @returns {string} - The text with mentions and issue numbers replaced by Markdown links.
 */
function replaceText(toReplace: string): string {
  // Initialize with the original text
  let text = toReplace;

  // Regular expression to find "by @username" and replace "@username" with a Markdown link to the user's GitHub profile
  const userRegex = /by (@([a-zA-Z0-9\-_]+))/g;
  text = text.replace(userRegex, (match, mention, username) => {
    return `by [@${username}](https://github.com/${username})`;
  });

  // Regular expression to find "in #issueNumber" and replace "#issueNumber" with a Markdown link to the specific issue
  const issueRegex = /in (#(\d+))/g;
  text = text.replace(issueRegex, (match, issue, number) => {
    return `in [#${number}](https://github.com/umijs/mako/pull/${number})`;
  });

  // Return the modified text
  return text;
}