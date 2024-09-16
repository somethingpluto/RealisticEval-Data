function getFileIdFromUrl(url) {
    // Define a regular expression to match the file ID in the URL
    const regex = /\/upload\/v\d+\/([^/]+)\./;

    // Execute the regex on the URL
    const match = url.match(regex);

    // Return the file ID if a match was found, otherwise return null
    return match ? match[1] : null;
}