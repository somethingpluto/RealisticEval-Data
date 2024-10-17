function convertCsvValues(row) {
    /**
     * Convert numeric values in a CSV row from string format to a standardized format.
     *
     * @param {Object} row - An object representing a row of CSV data where
     *                       keys are column names and values are strings.
     * @returns {Object} - A new object with values converted:
     *                     - Numeric strings have commas replaced with dots.
     *                     - Non-numeric strings are set to null.
     */
    const convertedRow = {};

    for (const [key, value] of Object.entries(row)) {
        // Check if the value is numeric with possible comma and negative sign
        const isNumeric = value.replace(',', '', 1).replace('-', '', 1).match(/^\d+$/);

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