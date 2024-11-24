function extractDateFromFileName(fileName) {
    const datePattern = /\d{4}-\d{2}-\d{2}/;

    // Search for the date pattern in the file name
    const match = fileName.match(datePattern);

    // If a match is found, return the matched date; otherwise, return null
    return match ? match[0] : null;
}