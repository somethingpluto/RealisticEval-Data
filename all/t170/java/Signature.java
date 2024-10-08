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
 * @param html The input string containing HTML content.
 * @return A string formatted in Markdown, reflecting the input HTML structure.
 */
public static String convert(String html) {}