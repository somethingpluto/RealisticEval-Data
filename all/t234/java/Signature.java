/**
 * Appends a new row to a CSV file if there isn't a row with matching values in the first three columns.
 *
 * @param fileHandler The file handler of the CSV file opened in read-plus mode ('r+').
 * @param reader The CSV reader object for reading existing rows.
 * @param rowCandidate The list containing the new row to be appended.
 */
public static void appendOrSkipRow(PrintWriter fileHandler, List<String> reader, List<String> rowCandidate) {}