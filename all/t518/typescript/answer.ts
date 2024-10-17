import { Optional } from 'typescript-optional'; // Assuming a library for Optional

function convertCsvValues(row: Record<string, string>): Record<string, string | null> {
    /**
     * Convert numeric values in a CSV row from string format to a standardized format.
     *
     * @param row - A dictionary representing a row of CSV data where keys are column names and values are strings.
     * @returns A new dictionary with values converted:
     *          - Numeric strings have commas replaced with dots.
     *          - Non-numeric strings are set to null.
     */
    const convertedRow: Record<string, string | null> = {};

    for (const [key, value] of Object.entries(row)) {
        // Check if the value is numeric with possible comma and negative sign
        const isNumeric = value.replace(',', '').replace('-', '').match(/^-?\d+(\.\d+)?$/) !== null;

        if (isNumeric) {
            // Replace comma with dot for numeric conversion
            convertedRow[key] = value.replace(',', '.');
        } else {
            // Set to null if not a valid number
            convertedRow[key] = null;
        }
    }

    return convertedRow;
}