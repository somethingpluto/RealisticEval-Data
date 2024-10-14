package org.real.temp;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;

import org.junit.Test;

public class Tester {

    @Test
    public void testValidPngBase64() {
        String validPng = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA";
        assertTrue(ImageValidator.isBase64Image(validPng));
    }

    @Test
    public void testValidJpegBase64() {
        String validJpeg = "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQEAAAAAA";
        assertTrue(ImageValidator.isBase64Image(validJpeg));
    }

    @Test
    public void testInvalidFormat() {
        String invalidFormat = "data:text/plain;base64,SGVsbG8gd29ybGQ=";
        assertFalse(ImageValidator.isBase64Image(invalidFormat));
    }

    @Test
    public void testInvalidBase64Characters() {
        String invalidBase64 = "data:image/png;base64,invalidBase64String@#%";
        assertFalse(ImageValidator.isBase64Image(invalidBase64));
    }

    @Test
    public void testEmptyString() {
        assertFalse(ImageValidator.isBase64Image(""));
    }

    @Test
    public void testNullInput() {
        assertFalse(ImageValidator.isBase64Image(null));
    }
}