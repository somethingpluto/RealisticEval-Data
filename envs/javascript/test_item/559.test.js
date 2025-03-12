/**
 * Checks whether a file name is a C++ header file.
 *
 * @param {string} fileName - The name of the file to check.
 * @returns {boolean} - Returns true if the file is a C++ header file, false otherwise.
 */
function isCppHeaderFile(fileName) {
    // Define the common C++ header file extensions
    const cppHeaderExtensions = ['.h', '.hpp', '.hh', '.hxx'];

    // Check if the file name ends with any of the C++ header file extensions
    for (let extension of cppHeaderExtensions) {
        if (fileName.endsWith(extension)) {
            return true;
        }
    }

    // If no matching extension is found, return false
    return false;
}
describe('isCppHeaderFile', () => {
    test('returns true for a .h file', () => {
        expect(isCppHeaderFile('example.h')).toBe(true);
    });

    test('returns true for a .hpp file', () => {
        expect(isCppHeaderFile('example.hpp')).toBe(true);
    });



    test('returns false for a non-header file extension', () => {
        expect(isCppHeaderFile('example.txt')).toBe(false);
    });

    test('returns false for a file without an extension', () => {
        expect(isCppHeaderFile('example')).toBe(false);
    });

    test('returns false for a .c file', () => {
        expect(isCppHeaderFile('example.c')).toBe(false);
    });

});

