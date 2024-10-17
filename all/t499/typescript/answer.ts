import * as re from 'xregexp';

function cleanPattern(x: string | any, pattern: string): number | '' {
    /**
     * Extracts a numeric value from the input string based on the given regex pattern.
     *
     * @param x - The input from which to extract the value. It will be converted to a string.
     * @param pattern - The regular expression pattern to use for matching.
     * @returns The extracted weight value as a number if a match is found, otherwise an empty string.
     */
    // Convert input to string
    const inputString = String(x);

    // Search for the pattern in the input string
    const match = re.exec(inputString, new RegExp(pattern));

    if (match && match[1]) {
        // Extract the weight value from the first matching group
        const weight = match[1];
        try {
            // Convert the weight to a float and return it
            const weightValue = parseFloat(weight);
            return weightValue;
        } catch (error) {
            // Handle cases where conversion to float fails
            console.warn(`Warning: Unable to convert '${weight}' to float.`);
            return '';
        }
    } else {
        return '';  // Return empty string if no match is found
    }
}