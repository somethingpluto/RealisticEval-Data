import { simplifyWindowsPath } from './simplifyWindowsPath';

describe('simplifyWindowsPath', () => {
    it('should handle a simple path', () => {
        expect(simplifyWindowsPath('C:\\Users\\User\\file.txt')).toBe('C_Users_User_file.txt');
    });

    it('should handle a path with spaces', () => {
        expect(simplifyWindowsPath('E:\\New Folder\\my file.docx')).toBe('E_New Folder_my file.docx');
    });

    it('should handle a path with special characters', () => {
        expect(simplifyWindowsPath('D:\\question\\new-year@2020\\report#1.pdf')).toBe('D_question_new-year@2020_report#1.pdf');
    });

    it('should handle nested directories', () => {
        expect(simplifyWindowsPath('G:\\folder1\\folder2\\folder3\\file.jpeg')).toBe('G_folder1_folder2_folder3_file.jpeg');
    });
});