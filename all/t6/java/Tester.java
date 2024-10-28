package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSimplePath() {
        assertEquals("C_Users_User_file.txt", simplifyWindowsPath("C:\\Users\\User\\file.txt"));
    }

    @Test
    public void testSimplePath2() {
        assertEquals("D_User_file.txt", simplifyWindowsPath("D:\\User\\file.txt"));
    }

    @Test
    public void testPathWithSpaces() {
        assertEquals("E_New Folder_my file.docx", simplifyWindowsPath("E:\\New Folder\\my file.docx"));
    }

    @Test
    public void testNestedDirectories() {
        assertEquals("G_folder1_folder2_folder3_file.jpeg", simplifyWindowsPath("G:\\folder1\\folder2\\folder3\\file.jpeg"));
    }

    @Test
    public void testPathWithSingleBackslash(){
        assertEquals("F_",simplifyWindowsPath("F:\\"));
    }
}