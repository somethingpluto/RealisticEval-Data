package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
/**
 * Test class for the file size converter.
 */
public class Tester {

    /**
     * Tests the conversion of zero bytes.
     */
    @Test
    public void testZeroBytes() {
        assertEquals("0B", convertFileSize(0));
    }

    /**
     * Tests the conversion of bytes less than 1KB.
     */
    @Test
    public void testBytesLessThan1KB() {
        assertEquals("512B", convertFileSize(512));
    }

    /**
     * Tests the conversion of exactly 1KB.
     */
    @Test
    public void testExactly1KB() {
        assertEquals("1KB", convertFileSize(1024));
    }

    /**
     * Tests the conversion of 2KB.
     */
    @Test
    public void test2KB() {
        assertEquals("2KB", convertFileSize(2048));
    }

    /**
     * Tests the conversion of exactly 1MB.
     */
    @Test
    public void testExactly1MB() {
        assertEquals("1MB", convertFileSize(1048576));
    }

    /**
     * Tests the conversion of 5MB.
     */
    @Test
    public void test5MB() {
        assertEquals("5MB", convertFileSize(5242880));
    }

    /**
     * Tests the conversion of exactly 1GB.
     */
    @Test
    public void testExactly1GB() {
        assertEquals("1GB", convertFileSize(1073741824L));
    }
}