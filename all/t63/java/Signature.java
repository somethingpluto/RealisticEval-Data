/**
 * Converts a DataFrame object to a table in Markdown format.
 * <p>
 * Example:
 * Input: DataFrame with columns {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
 * Output:
 * <pre>
 * | Name | Age |
 * | --- | --- |
 * | Alice | 25 |
 * | Bob | 30 |
 * </pre>
 *
 * @param data The data represented as a List of Lists, where each inner list represents a row.
 * @param columns The column names of the DataFrame.
 * @param mdPath The output Markdown file path.
 * @return The generated Markdown file content as a string.
 */
public static String dataframeToMarkdown(List<List<String>> data, List<String> columns, String mdPath) {}