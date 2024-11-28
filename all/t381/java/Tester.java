package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import static org.junit.Assert.assertThrows;
import static org.real.temp.Answer.*;
/**
 * Test class for the extractEmailDetails method.
 */
public class Tester {

    /**
     * Tests extracting details from a typical email address.
     */
    @Test
    public void testValidEmail() {
        // Test with a typical email address
        String email = "user@example.com";
        String[] expected = {"user", "example.com"};
        String[] result = extractEmailDetails(email);
        assertArrayEquals(expected, result);
    }

    /**
     * Tests extracting details from an email that includes a subdomain.
     */
    @Test
    public void testValidEmailWithSubdomain() {
        // Test with an email that includes a subdomain
        String email = "user@mail.office.com";
        String[] expected = {"user", "mail.office.com"};
        String[] result = extractEmailDetails(email);
        assertArrayEquals(expected, result);
    }

    /**
     * Tests extracting details from an email that lacks an '@' symbol.
     */
    @Test
    public void testEmailWithoutAtSymbol() {
        // Test with an email that lacks an '@' symbol
        String email = "userexample.com";
        assertThrows(IllegalArgumentException.class, () -> extractEmailDetails(email));
    }

    /**
     * Tests extracting details from an empty string as an email.
     */
    @Test
    public void testEmptyEmail() {
        // Test with an empty string as an email
        String email = "";
        assertThrows(IllegalArgumentException.class, () -> extractEmailDetails(email));
    }
}