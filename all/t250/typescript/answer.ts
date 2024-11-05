function invertDictionary(originalDict: Record<string, string | string[]>): Record<string, string | string[]> {
    const newDict: Record<string, string | string[]> = {};
    for (const key in originalDict) {
        if (originalDict.hasOwnProperty(key)) {
            const value = originalDict[key];
            if (!(value in newDict)) {
                newDict[value] = key;
            } else {
                // If the value already exists as a key, we need to append to or create a list
                if (!Array.isArray(newDict[value])) {
                    newDict[value] = [newDict[value]];
                }
                (newDict[value] as string[]).push(key);
            }
        }
    }
    return newDict;
}