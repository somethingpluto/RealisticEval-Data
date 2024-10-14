package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;

public class Tester {

    @Test
    public void validUsernameWithAlphanumericCharacters() {
        assertTrue(UsernameValidator.isValidUsername("User123"));
    }

    @Test
    public void validUsernameWithSpaces() {
        assertTrue(UsernameValidator.isValidUsername("User 123"));
    }

    @Test
    public void invalidUsernameThatIsTooShort() {
        assertFalse(UsernameValidator.isValidUsername("User"));
    }

    @Test
    public void invalidUsernameThatIsTooLong() {
        assertFalse(UsernameValidator.isValidUsername("ThisIsAVeryLongUsername"));
    }

    @Test
    public void invalidUsernameWithSpecialCharacters() {
        assertFalse(UsernameValidator.isValidUsername("User!"));
    }

    @Test
    public void invalidUsernameWithOnlySpaces() {
        assertFalse(UsernameValidator.isValidUsername("     "));
    }

    @Test
    public void invalidInputType() {
        // Since the method expects a String, we can test invalid input type
        assertFalse(UsernameValidator.isValidUsername(Integer.toString(12345)));
    }
}