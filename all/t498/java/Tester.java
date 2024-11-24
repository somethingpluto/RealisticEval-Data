package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testEmptyString() {
        // Test the MD5 hash of an empty string.
        assertEquals("d41d8cd98f00b204e9800998ecf8427e", computeMD5(""));
    }

    @Test
    public void testSimpleString() {
        // Test the MD5 hash of a simple string.
        assertEquals("65a8e27d8879283831b664bd8b7f0ad4", computeMD5("Hello, World!"));
    }

    @Test
    public void testNumericString() {
        // Test the MD5 hash of a numeric string.
        assertEquals("e10adc3949ba59abbe56e057f20f883e", computeMD5("123456"));
    }

    @Test
    public void testSpecialCharacters() {
        // Test the MD5 hash of a string with special characters.
        assertEquals("05b28d17a7b6e7024b6e5d8cc43a8bf7", computeMD5("!@#$%^&*()"));
    }

    @Test
    public void testLongString() {
        // Test the MD5 hash of a long string.
        String longString = "a".repeat(1000);  // A string of 1000 'a' characters
        String expectedHash = "cabe45dcc9ae5b66ba86600cca6b8ba8";  // MD5 of 'aaaa....' (1000 'a's)
        assertEquals(expectedHash, computeMD5(longString));
    }
}