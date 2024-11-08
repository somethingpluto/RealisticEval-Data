package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testValidSimpleEmail() {
        boolean result = isValidEmail("test@example.com");
        assertTrue(result); // 'test@example.com' is a valid email
    }

    @Test
    public void testValidEmailWithSubdomain() {
        boolean result = isValidEmail("user@mail.example.com");
        assertTrue(result); // 'user@mail.example.com' is a valid email
    }

    @Test
    public void testEmailMissingAtSymbol() {
        boolean result = isValidEmail("invalid-email.com");
        assertFalse(result); // 'invalid-email.com' is missing the @ symbol
    }

    @Test
    public void testEmailMissingDomainPart() {
        boolean result = isValidEmail("user@.com");
        assertFalse(result); // 'user@.com' is missing a valid domain name
    }

    @Test
    public void testEmailWithSpaces() {
        boolean result = isValidEmail("user name@example.com");
        assertFalse(result); // 'user name@example.com' contains spaces
    }
}