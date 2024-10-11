package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {
    @Test
    public void testSimplifyWindowsPath() {
        assertEquals("C_Users_User_file.txt", simplifyWindowsPath("C:\\Users\\User\\file.txt"));
        assertEquals("D_Documents_folder_document.pdf", simplifyWindowsPath("D:\\Documents\\folder\\document.pdf"));
        assertEquals("_root_folder_root_subfolder_file.docx", simplifyWindowsPath("C:\\root_folder\\root_subfolder\\file.docx"));
    }
}