/**
 * Convert numeric values in a CSV row from string format to a standardized format.
 *
 * @param row - A dictionary representing a row of CSV data where keys are column names and values are strings.
 * @returns A new dictionary with values converted:
 *          - Numeric strings have commas replaced with dots.
 *          - Non-numeric strings are set to null.
 */
function convertCsvValues(row: Record<string, string>): Record<string, string | null> {

}