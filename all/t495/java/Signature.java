/**
 * Filters website content to include lines containing any of the specified keywords as whole words,
 * along with a specified number of lines before and after for context. This version uses regular expressions
 * to ensure exact, whole word matching and respects case sensitivity.
 *
 * @param content       The full text content of the website.
 * @param keywords      A list of strings to search for within the content.
 * @param linesBefore   Number of lines to include before a matching line.
 * @param linesAfter    Number of lines to include after a matching line.
 * @return              A string containing the filtered content with additional context.
 */
public static String filterContentWithContext(String content, List<String> keywords, int linesBefore, int linesAfter) {

}