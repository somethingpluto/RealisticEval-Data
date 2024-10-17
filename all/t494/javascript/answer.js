function cleanDictionary(inputDict) {
    /**
     * Cleans the input object by removing keys with invalid values.
     * Valid values are non-NaN, non-null, and non-whitespace strings.
     *
     * @param {Object} inputDict - An object to be cleaned.
     * @return {Object} A new object containing only valid values.
     */
    const cleanedDict = {};

    for (const [key, value] of Object.entries(inputDict)) {
        // Check if the value is not null and not just whitespace
        if (value !== null && (typeof value === 'string' && value.trim().length > 0)) {
            // Check if value is a number (int or float) and is not NaN
            if (!(typeof value === 'number' && Number.isNaN(value))) {
                cleanedDict[key] = value;
            }
        }
    }

    return cleanedDict;
}