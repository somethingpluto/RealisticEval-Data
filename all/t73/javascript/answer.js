/**
 * Convert an object of arrays into an array of objects.
 *
 * @param {Object} dictOfLists - An object where each key has an array as its value.
 * @returns {Array} - An array where each item is an object formed by corresponding elements of arrays in the input object.
 * @throws {Error} - If arrays in the object are of different lengths.
 */
function dictOfListsToListOfDicts(dictOfLists) {
    if (Object.keys(dictOfLists).length === 0) {
        return [];
    }
    const lengths = Object.values(dictOfLists).map(arr => arr.length);
    const uniqueLengths = new Set(lengths);
    if (uniqueLengths.size !== 1) {
        throw new Error("All arrays in the object must have the same length.");
    }
    const keys = Object.keys(dictOfLists);
    const listLength = lengths[0];
    const listOfDicts = [];
    for (let i = 0; i < listLength; i++) {
        const dict = {};
        for (let j = 0; j < keys.length; j++) {
            const key = keys[j];
            dict[key] = dictOfLists[key][i];
        }
        listOfDicts.push(dict);
    }
    return listOfDicts;
}