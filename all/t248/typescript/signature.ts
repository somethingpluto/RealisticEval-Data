/**
 * Removes the corresponding sensitive questions in the given dictionary based on the given keyToRemove array.
 *
 * @param {QuestionDict} data - The original question dictionary.
 * @param {string[]} keyToRemove - The array of keys to remove.
 * @returns {QuestionDict} - The dictionary with the specified keys removed.
 */
function sanitizeData(data: QuestionDict, keyToRemove: string[] = []): QuestionDict {
    return Object.keys(data).reduce((acc, key) => {
        if (!keyToRemove.includes(key)) {
            acc[key] = data[key];
        }
        return acc;
    }, {} as QuestionDict);
}