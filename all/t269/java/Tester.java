package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
/**
 * Test class for verifying the compliance of IP addresses.
 */
public class Tester {

    /**
     * Tests that private IP addresses return true.
     */
    @Test
    public void testPrivateIP() {
        // Test that private IPs return true
        assertTrue(isCompliantIP("192.168.1.1"));
    }

    /**
     * Tests that public IP addresses return false.
     */
    @Test
    public void testPublicIP() {
        // Test that public IPs return false
        assertFalse(isCompliantIP("8.8.8.8"));
    }

    /**
     * Tests that invalid IP strings return false.
     */
    @Test
    public void testInvalidIP() {
        // Test that invalid IP strings return false
        assertFalse(isCompliantIP("999.999.999.999"));
    }
}