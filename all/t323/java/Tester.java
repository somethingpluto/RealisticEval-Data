package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testValidUsernameWithLettersNumbersAndUnderscores() {
        boolean result = isValidUsername("user_123");
        assertTrue(result); // 'user_123' is a valid username
    }

    @Test
    public void testValidUsernameWithOnlyLetters() {
        boolean result = isValidUsername("username");
        assertTrue(result); // 'username' is a valid username
    }

    @Test
    public void testUsernameWithSpecialCharacters() {
        boolean result = isValidUsername("user-name");
        assertFalse(result); // 'user-name' contains a hyphen
    }

    @Test
    public void testUsernameWithSpaces() {
        boolean result = isValidUsername("user name");
        assertFalse(result); // 'user name' contains spaces
    }

    @Test
    public void testValidUsernameWithOnlyNumbers() {
        boolean result = isValidUsername("12345");
        assertTrue(result); // '12345' is a valid username
    }
}