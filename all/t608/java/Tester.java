package org.real.temp;

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testValidEmail1() {
        assertTrue(Answer.isValidEmail("example@test.com"), "Valid email should return true");
    }

    @Test
    public void testValidEmail2() {
        assertTrue(Answer.isValidEmail("user.name+tag+sorting@example.com"), "Valid email should return true");
    }

    @Test
    public void testValidEmail3() {
        assertTrue(Answer.isValidEmail("user@subdomain.example.com"), "Valid email with subdomain should return true");
    }

    @Test
    public void testInvalidEmail1() {
        assertFalse(Answer.isValidEmail("invalid-email@.com"), "Invalid email should return false");
    }

    @Test
    public void testInvalidEmail2() {
        assertFalse(Answer.isValidEmail("invalid@domain@domain.com"), "Invalid email should return false");
    }


    @Test
    public void testNullEmail() {
        assertFalse(Answer.isValidEmail(null), "Null email should return false");
    }
}