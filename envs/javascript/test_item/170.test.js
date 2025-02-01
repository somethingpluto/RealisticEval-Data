/**
 * Converts a string containing HTML to a Markdown-formatted string.
 *
 * 1. Line breaks (<br> or <br/>): Replaced with newline characters.
 * 2. Paragraphs (<p> and </p>): Opening <p> tags are removed, while closing
 *    </p> tags are replaced with two newline characters to separate paragraphs.
 * 3. Strong emphasis (<strong> and </strong>): Replaced with double asterisks (**).
 * 4. Italics (<em> and </em>): Replaced with single asterisks (*).
 * 5. Underlined text (<u> and </u>): Replaced with single asterisks (*)
 *    as underlining is not supported in Markdown.
 * 6. Code snippets (<code> and </code>): Replaced with backticks (`).
 * 7. Unordered lists (<ul> and </ul>): Opening and closing tags are removed.
 * 8. Ordered lists (<ol> and </ol>): Opening and closing tags are removed.
 * 9. List items (<li>): Opening <li> tags are replaced with an asterisk followed
 *    by a space, while closing </li> tags are replaced with a newline character.
 * 10. Hyperlinks (<a href="...">...</a>): Replaced with the Markdown format
 *     [text](URL), where "text" is the anchor text and "URL" is the link target.
 *
 * @param {string} html - The input string containing HTML content.
 * @return {string} A string formatted in Markdown, reflecting the input HTML structure.
 */
function convert(html) {
  // Replace line breaks
  html = html.replace(/<br\s*\/?>/gi, '\n');

  // Replace paragraphs
  html = html.replace(/<p>/gi, '');
  html = html.replace(/<\/p>/gi, '\n\n');

  // Replace strong emphasis
  html = html.replace(/<strong>/gi, '**');
  html = html.replace(/<\/strong>/gi, '**');

  // Replace italics
  html = html.replace(/<em>/gi, '*');
  html = html.replace(/<\/em>/gi, '*');

  // Replace underlined text
  html = html.replace(/<u>/gi, '*');
  html = html.replace(/<\/u>/gi, '*');

  // Replace code snippets
  html = html.replace(/<code>/gi, '`');
  html = html.replace(/<\/code>/gi, '`');

  // Replace unordered lists
  html = html.replace(/<\/?ul>/gi, '');

  // Replace ordered lists
  html = html.replace(/<\/?ol>/gi, '');

  // Replace list items
  html = html.replace(/<li>/gi, '* ');
  html = html.replace(/<\/li>/gi, '\n');

  // Replace hyperlinks
  html = html.replace(/<a href="([^"]*)">([^<]*)<\/a>/gi, '[$2]($1)');

  return html;
}
describe('HTML to Markdown Converter', () => {
  
    test('testSimpleLineBreak', () => {
        const input = 'Hello<br>World';
        const expectedOutput = 'Hello\nWorld';
        expect(convert(input)).toBe(expectedOutput);
    });

    test('testStrongTags', () => {
        const input = 'This is <strong>important</strong> text.';
        const expectedOutput = 'This is **important** text.';
        expect(convert(input)).toBe(expectedOutput);
    });

    test('testEmphasisTags', () => {
        const input = 'This is <em>emphasized</em> text.';
        const expectedOutput = 'This is *emphasized* text.';
        expect(convert(input)).toBe(expectedOutput);
    });

    test('testUnorderedList', () => {
        const input = '<ul><li>Item 1</li><li>Item 2</li></ul>';
        const expectedOutput = '* Item 1\n* Item 2';
        expect(convert(input)).toBe(expectedOutput);
    });

    test('testAnchorTags', () => {
        const input = 'Check this link: <a href="http://example.com">Example</a>.';
        const expectedOutput = 'Check this link: [Example](http://example.com).';
        expect(convert(input)).toBe(expectedOutput);
    });
});
