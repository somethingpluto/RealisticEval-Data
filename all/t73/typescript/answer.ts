function dictOfListsToListOfDicts(dictOfLists: { [key: string]: any[] }): any[][] {
    // Check if all lists are of the same length
    if (Object.keys(dictOfLists).length === 0) {
        return [];
    }
    const lengths = Object.values(dictOfLists).map(lst => lst.length);
    const uniqueLengths = new Set(lengths);
    if (uniqueLengths.size !== 1) {
        throw new Error("All lists in the dictionary must have the same length.");
    }

    // Using zip to iterate over lists simultaneously
    const keys = Object.keys(dictOfLists);
    const listOfDicts = keys[0]
        ? keys.map((_, index) => {
            return keys.reduce((acc, key) => {
                acc[key] = dictOfLists[key][index];
                return acc;
            }, {} as { [key: string]: any });
        })
        : [];

    return listOfDicts;
}
