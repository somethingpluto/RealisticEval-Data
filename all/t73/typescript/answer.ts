/**
 * Convert an object of arrays into an array of objects.
 *
 * @param {Record<string, any[]>} dictOfLists - An object where each key has an array as its value.
 * @returns {Array<Record<string, any>>} - An array where each item is an object formed by corresponding elements of arrays in the input object.
 * @throws {Error} - If arrays in the object are of different lengths.
 */
function dictOfListsToListOfDicts(dictOfLists: Record<string, any[]>): Array<Record<string, any>> {
    if (Object.keys(dictOfLists).length === 0) {
        return [];
    }

    const lengths: number[] = Object.values(dictOfLists).map(arr => arr.length);
    const uniqueLengths: Set<number> = new Set(lengths);
    
    if (uniqueLengths.size !== 1) {
        throw new Error("All arrays in the object must have the same length.");
    }

    const keys: string[] = Object.keys(dictOfLists);
    const listLength: number = lengths[0];
    const listOfDicts: Array<Record<string, any>> = [];

    for (let i = 0; i < listLength; i++) {
        const dict: Record<string, any> = {};
        for (let j = 0; j < keys.length; j++) {
            const key: string = keys[j];
            dict[key] = dictOfLists[key][i];
        }
        listOfDicts.push(dict);
    }

    return listOfDicts;
}
