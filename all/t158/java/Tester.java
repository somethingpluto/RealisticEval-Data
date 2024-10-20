package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testGetFileExtension_standardFile() {
        assertEquals("txt", getFileExtension("example.txt"));
    }

    @Test
    public void testGetFileExtension_noExtension() {
        assertEquals("", getFileExtension("example"));
    }

    @Test
    public void testGetFileExtension_multipleDots() {
        assertEquals("jpg", getFileExtension("example.with.many.dots.jpg"));
    }

    @Test
    public void testGetFileExtension_trailingDot() {
        assertEquals("", getFileExtension("example."));
    }

    @Test
    public void testGetFileExtension_caseSensitivity() {
        assertEquals("JPG", getFileExtension("example.JPG"));
    }
}