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