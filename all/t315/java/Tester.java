package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testValidUrlWithFileId() {
        String url = "https://example.com/download?fileId=12345";
        assertEquals("12345", getFileIdFromUrl(url));
    }

    @Test
    public void testMissingFileIdParameter() {
        String url = "https://example.com/download";
        assertEquals(null, getFileIdFromUrl(url));
    }

    @Test
    public void testEmptyFileIdParameter() {
        String url = "https://example.com/download?fileId=";
        assertEquals(null, getFileIdFromUrl(url));
    }

    @Test
    public void testMalformedUrl() {
        String url = "https://example.com/download?fileId=12345&otherParam";
        assertEquals("12345", getFileIdFromUrl(url)); // Adjust as necessary
    }
}