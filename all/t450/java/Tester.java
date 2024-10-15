package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;

public class Tester {

    @Test
    public void testValidPassword() {
        assertTrue(PasswordValidator.isValidPassword("Password1!"));
    }

    @Test
    public void testPasswordWithoutNumber() {
        assertFalse(PasswordValidator.isValidPassword("Password!"));
    }

    @Test
    public void testPasswordWithoutUppercase() {
        assertFalse(PasswordValidator.isValidPassword("password1!"));
    }

    @Test
    public void testPasswordWithoutLowercase() {
        assertFalse(PasswordValidator.isValidPassword("PASSWORD1!"));
    }

    @Test
    public void testPasswordWithoutPunctuation() {
        assertFalse(PasswordValidator.isValidPassword("Password1"));
    }

    @Test
    public void testPasswordShorterThan8Characters() {
        assertFalse(PasswordValidator.isValidPassword("Pass1!"));
    }
}