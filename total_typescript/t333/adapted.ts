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