function sanitizeFilename(filename) {
    /**
     * Remove illegal characters from Windows file path string.
     *
     * @param {string} filename - The original filename string to be sanitized.
     * @returns {string} A sanitized string that is safe to use as a Windows filename.
     */
    // Define the illegal characters for Windows filenames
    const illegalCharsPattern = /[<>:"/\\|?*\x00-\x1F]/g;

    // Replace illegal characters with an underscore
    let sanitized = filename.replace(illegalCharsPattern, '_');

    // Optionally, you can also limit the length of the filename
    // Windows has a maximum path length of 260 characters
    const maxLength = 255;
    if (sanitized.length > maxLength) {
        sanitized = sanitized.substring(0, maxLength);
    }

    return sanitized;
}