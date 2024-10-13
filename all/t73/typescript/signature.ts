/**
 * Convert a dictionary of lists into a list of dictionaries.
 * 
 * @param dictOfLists - A dictionary where each key has a list as its value.
 * @returns A list where each item is a dictionary formed by corresponding elements of lists in the input dictionary.
 * @throws {Error} If lists in the dictionary are of different lengths.
 */
function dictOfListsToListOfDicts(dictOfLists: { [key: string]: any[] }): { [key: string]: any }[] {}