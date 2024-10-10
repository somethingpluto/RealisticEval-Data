function dictOfListsToListOfDicts(dictOfLists: {[key: string]: any[]}): { [key: string]: any }[] {
    const keys = Object.keys(dictOfLists);
    const length = Math.max(...keys.map(key => dictOfLists[key].length));

    return Array.from({ length }, (_, i) => {
        const result: { [key: string]: any } = {};
        for (const key of keys) {
            if (i < dictOfLists[key].length) {
                result[key] = dictOfLists[key][i];
            }
        }
        return result;
    });
}