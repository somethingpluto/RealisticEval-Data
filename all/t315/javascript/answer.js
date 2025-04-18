/**
 * Extract the file ID from the given URL query args
 *
 * @param {string} url - The URL from which the file ID is to be extracted.
 * @returns {string|null} - The extracted file ID if present, otherwise null if the URL does not conform to the expected format.
 */
function getFileIdFromUrl(url) {
    try {
        const urlObject = new URL(url); // Create a URL object to parse the URL.

        // Extract the file ID from the query parameters using 'fileId' as the key
        const fileId = urlObject.searchParams.get('fileId');

        // Return the decoded file ID if found, otherwise null
        return fileId ? decodeURIComponent(fileId) : null;
    } catch (error) {
        console.error('Invalid URL:', error);
        return null; // Return null if the URL is invalid or an error occurs.
    }
}