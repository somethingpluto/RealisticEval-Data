describe('simplifyWindowsPath', () => {
    test('converts a simple Windows path', () => {
        expect(simplifyWindowsPath('C:\\Users\\User\\file.txt')).toBe('C_Users_User_file.txt');
    });

    test('converts a path with spaces', () => {
        expect(simplifyWindowsPath('E:\\New Folder\\my file.docx')).toBe('E_New Folder_my file.docx');
    });

    test('converts a path with special characters', () => {
        expect(simplifyWindowsPath('D:\\question\\new-year@2020\\report#1.pdf'))
            .toBe('D_question_new-year@2020_report#1.pdf');
    });

    test('converts nested directories', () => {
        expect(simplifyWindowsPath('G:\\folder1\\folder2\\folder3\\file.jpeg'))
            .toBe('G_folder1_folder2_folder3_file.jpeg');
    });
});