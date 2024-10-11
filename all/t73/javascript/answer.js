function dictOfListsToListOfDicts(dictOfLists) {
    // Get all keys from the dictionary
    const keys = Object.keys(dictOfLists);

    // Find the maximum length among all lists to determine how many dictionaries we need
    const maxLength = Math.max(...keys.map(key => dictOfLists[key].length));

    // Initialize an array to hold the resulting list of dictionaries
    const listOfDicts = [];

    // Iterate over each index up to the maximum length
    for (let i = 0; i < maxLength; i++) {
        const newDict = {};

        // Iterate over each key and add the element at the current index to the new dictionary
        keys.forEach(key => {
            if (i < dictOfLists[key].length) {
                newDict[key] = dictOfLists[key][i];
            }
        });

        // Add the new dictionary to the list
        listOfDicts.push(newDict);
    }

    return listOfDicts;
}