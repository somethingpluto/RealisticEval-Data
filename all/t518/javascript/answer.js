function convertCsvValues(row) {
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