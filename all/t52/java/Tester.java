package org.real.temp;

import org.junit.Test; // Change to JUnit 4 Test import

import static org.junit.Assert.assertEquals; // Change to JUnit 4 assertion
import static org.real.temp.Answer.*;

/**
 * Test cases for the renameFilePath method.
 */
public class Tester {

    /**
     * Tests renaming a file path with a colon in the filename.
     */
    @Test
    public void testRenameWithColonInFilename() {
        // Test path with colon in the filename
        String path = "C:\\Users\\example\\Documents\\report:2023.txt";
        String expected = "C:\\Users\\example\\Documents\\report_2023.txt";
        assertEquals(expected, renameFilePath(path));
    }

    /**
     * Tests renaming a file path without a colon in the filename.
     */
    @Test
    public void testRenameWithoutColonInFilename() {
        // Test path without colon in the filename
        String path = "C:\\Users\\example\\Documents\\report2023.txt";
        String expected = "C:\\Users\\example\\Documents\\report2023.txt";
        assertEquals(expected, renameFilePath(path));
    }

    /**
     * Tests renaming a file path with multiple colons in the filename.
     */
    @Test
    public void testRenameWithMultipleColonsInFilename() {
        // Test path with multiple colons in the filename
        String path = "C:\\Users\\example\\Documents\\project:report:2023.txt";
        String expected = "C:\\Users\\example\\Documents\\project_report_2023.txt";
        assertEquals(expected, renameFilePath(path));
    }

    /**
     * Tests renaming a file path with a colon at the end of the filename.
     */
    @Test
    public void testRenameWithColonAtEndOfFilename() {
        // Test path with a colon at the end of the filename
        String path = "C:\\Users\\example\\Documents\\backup:";
        String expected = "C:\\Users\\example\\Documents\\backup_";
        assertEquals(expected, renameFilePath(path));
    }

    /**
     * Tests renaming a file path with a colon at the start of the filename.
     */
    @Test
    public void testRenameWithColonAtStartOfFilename() {
        // Test path with a colon at the start of the filename
        String path = "C:\\Users\\example\\Documents\\:initial_setup.txt";
        String expected = "C:\\Users\\example\\Documents\\_initial_setup.txt";
        assertEquals(expected, renameFilePath(path));
    }
}
