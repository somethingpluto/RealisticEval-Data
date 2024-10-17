function convertToShortFormat(inputStr: string): string {
    // Split the input string by underscores
    const segments = inputStr.split('_');

    // Extract the first character from each segment and join them
    const shortFormat = segments.map(segment => segment[0]).join('');

    return shortFormat;
}