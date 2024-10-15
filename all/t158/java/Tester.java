package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testGetFileExtension_standardFile() {
        assertEquals("txt", FileUtils.getFileExtension("example.txt"));
    }

    @Test
    public void testGetFileExtension_noExtension() {
        assertEquals("", FileUtils.getFileExtension("example"));
    }

    @Test
    public void testGetFileExtension_multipleDots() {
        assertEquals("jpg", FileUtils.getFileExtension("example.with.many.dots.jpg"));
    }

    @Test
    public void testGetFileExtension_trailingDot() {
        assertEquals("", FileUtils.getFileExtension("example."));
    }

    @Test
    public void testGetFileExtension_caseSensitivity() {
        assertEquals("JPG", FileUtils.getFileExtension("example.JPG"));
    }
}