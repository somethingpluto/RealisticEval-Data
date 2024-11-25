package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
/**
 * Test class for email validation.
 */
public class Tester {

    /**
     * Tests a valid email address.
     */
    @Test
    public void testValidEmail() {
        assertTrue(isValidEmail("test@example.com"));
    }

    /**
     * Tests a valid email address with a subdomain.
     */
    @Test
    public void testValidEmailWithSubdomain() {
        assertTrue(isValidEmail("user@subdomain.example.com"));
    }

    /**
     * Tests a valid email address with a plus tag.
     */
    @Test
    public void testValidEmailWithPlusTag() {
        assertTrue(isValidEmail("user.name+tag+sorting@example.com"));
    }

    /**
     * Tests an invalid email address missing a username.
     */
    @Test
    public void testInvalidEmailMissingUsername() {
        assertFalse(isValidEmail("@missingusername.com"));
    }

    /**
     * Tests an invalid email address missing an at symbol.
     */
    @Test
    public void testInvalidEmailMissingAtSymbol() {
        assertFalse(isValidEmail("missingatsign.com"));
    }

    /**
     * Tests an invalid email address with a too short top-level domain.
     */
    @Test
    public void testInvalidEmailTldTooShort() {
        assertFalse(isValidEmail("user@domain.c"));
    }

    /**
     * Tests an invalid email address with special characters.
     */
    @Test
    public void testInvalidEmailWithSpecialCharacters() {
        assertFalse(isValidEmail("user@domain.com!"));
    }
}