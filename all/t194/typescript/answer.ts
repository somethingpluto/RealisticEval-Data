function returnString(str: string | null | undefined): string {
    if (str === null || str === undefined) {
        throw new Error("Input string cannot be null or undefined.");
    }

    // Create a copy of the input string
    const copiedStr: string = str.slice();

    return copiedStr;
}