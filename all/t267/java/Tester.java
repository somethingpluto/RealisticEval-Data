package org.real.temp;

import junit.framework.TestCase;

public class Tester extends TestCase {

    public void testExtractSldTld() {
        String fqdn = "example.com";
        String[] result = DomainNameExtractor.extractSldTld(fqdn);
        assertEquals("example", result[0]);
        assertEquals("com", result[1]);

        fqdn = "sub.example.co.uk";
        result = DomainNameExtractor.extractSldTld(fqdn);
        assertEquals("example", result[0]);
        assertEquals("co.uk", result[1]);
    }

    public void testInvalidFQDN() {
        try {
            DomainNameExtractor.extractSldTld("invalid");
            fail("Expected IllegalArgumentException");
        } catch (IllegalArgumentException e) {
            // Expected exception
        }
    }
}