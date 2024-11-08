package org.real.temp;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
import org.junit.Test;

public class Tester {

    @Test
    public void testValidPassword() {
        assertTrue(isValidPassword("Password1!"));
    }

    @Test
    public void testPasswordWithoutNumber() {
        assertFalse(isValidPassword("Password!"));
    }

    @Test
    public void testPasswordWithoutUppercase() {
        assertFalse(isValidPassword("password1!"));
    }

    @Test
    public void testPasswordWithoutLowercase() {
        assertFalse(isValidPassword("PASSWORD1!"));
    }

    @Test
    public void testPasswordWithoutPunctuation() {
        assertFalse(isValidPassword("Password1"));
    }

    @Test
    public void testPasswordShorterThan8Characters() {
        assertFalse(isValidPassword("Pass1!"));
    }
}