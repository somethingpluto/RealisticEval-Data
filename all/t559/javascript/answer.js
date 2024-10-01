/**
 * Checks whether a file name is a C++ header file.
 *
 * @param {string} fileName - The name of the file to check.
 * @returns {boolean} - Returns true if the file is a C++ header file, false otherwise.
 */
function isCppHeaderFile(fileName) {
    // Define a regular expression to match C++ header file extensions
    const cppHeaderExtensions = /\.(h|hh|hpp|hxx)$/i;

    // Test the file name against the regular expression
    return cppHeaderExtensions.test(fileName);
}
