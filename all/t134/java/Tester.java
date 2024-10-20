package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void validUsernameWithAlphanumericCharacters() {
        assertTrue(isValidUsername("User123"));
    }

    @Test
    public void validUsernameWithSpaces() {
        assertTrue(isValidUsername("User 123"));
    }

    @Test
    public void invalidUsernameThatIsTooShort() {
        assertFalse(isValidUsername("User"));
    }

    @Test
    public void invalidUsernameThatIsTooLong() {
        assertFalse(isValidUsername("ThisIsAVeryLongUsername"));
    }

    @Test
    public void invalidUsernameWithSpecialCharacters() {
        assertFalse(isValidUsername("User!"));
    }

    @Test
    public void invalidUsernameWithOnlySpaces() {
        assertFalse(isValidUsername("     "));
    }

}