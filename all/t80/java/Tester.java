package org.real.temp;

import static junit.framework.TestCase.assertEquals;
import static org.real.temp.Answer.*;
import org.junit.Test;
public class Tester {

    @Test
    public void testValidFilename() {
        assertEquals("valid_filename.txt", sanitizeFilename("valid_filename.txt"));
    }

    @Test
    public void testIllegalCharacters() {
        assertEquals("invalid_filename_.txt", sanitizeFilename("invalid<filename>.txt"));
        assertEquals("file_name_with_illegal_chars_.txt", sanitizeFilename("file/name:with*illegal|chars?.txt"));
    }

    @Test
    public void testLongFilename() {
        String longFilename = "a".repeat(300) + ".txt";
        String sanitizedFilename = sanitizeFilename(longFilename);
        assertEquals(255, sanitizedFilename.length());
        assertEquals("a".repeat(255), sanitizedFilename);
    }

    @Test
    public void testEmptyFilename() {
        assertEquals("", sanitizeFilename(""));
    }
}