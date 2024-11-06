function removePartsOfString(...strings) {
    const results = [];
    for (const string of strings) {
        try {
            // Remove all characters before the first uppercase letter
            const uppercaseIndex = string.split('').findIndex(char => char === char.toUpperCase() && char !== char.toLowerCase());
            let modifiedString = string.substring(uppercaseIndex);

            // Remove all characters before the first lowercase letter
            const lowercaseIndex = modifiedString.split('').findIndex(char => char === char.toLowerCase() && char !== char.toUpperCase());
            modifiedString = modifiedString.substring(lowercaseIndex - 1);

            results.push(modifiedString);
        } catch (error) {
            // Handle cases where no uppercase or lowercase letters are found
            results.push(string);  // You may decide to push an empty string or an error message
        }
    }

    return results;
}
