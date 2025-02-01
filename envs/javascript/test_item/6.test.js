/**
 * Simplifies file paths in Windows systems into name strings.
 * For example:
 *     input: C:\Users\User\file.txt
 *     output: C_Users_User_file.txt
 * 
 * @param {string} path - The Windows file path string.
 * @returns {string} The simplified path string.
 */
function simplifyWindowsPath(path) {
    return path.replace(/\\/g, '_');
}
describe('TestSimplifyWindowsPath', () => {
    test('should simplify a simple path', () => {
        expect(simplifyWindowsPath('C:\\Users\\User\\file.txt')).toBe('C_Users_User_file.txt');
    });

    test('should simplify another simple path', () => {
        expect(simplifyWindowsPath('D:\\User\\file.txt')).toBe('D_User_file.txt');
    });

    test('should simplify a path with spaces', () => {
        expect(simplifyWindowsPath('E:\\New Folder\\my file.docx')).toBe('E_New Folder_my file.docx');
    });

    test('should simplify a nested directory path', () => {
        expect(simplifyWindowsPath('G:\\folder1\\folder2\\folder3\\file.jpeg')).toBe('G_folder1_folder2_folder3_file.jpeg');
    });
});
