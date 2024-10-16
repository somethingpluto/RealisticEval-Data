function returnString(str) {
    if (str == null) {
        throw new Error("Input string cannot be null or undefined.");
    }

    // Create a copy of the string
    const copiedStr = str.slice();

    return copiedStr;
}