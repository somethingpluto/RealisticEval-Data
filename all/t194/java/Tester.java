package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.junit.Assert.assertThrows;

public class Tester {

    @Test
    public void testReturnString_NonEmptyString() {
        String original = "Hello, World!";
        String copy = new Answer().returnString(original);
        assertEquals(original, copy);
    }

    @Test
    public void testReturnString_EmptyString() {
        String original = "";
        String copy = new Answer().returnString(original);
        assertEquals(original, copy);
    }

    @Test
    public void testReturnString_SpecialCharacters() {
        String original = "C++ is fun! @#$%^&*()";
        String copy = new Answer().returnString(original);
        assertEquals(original, copy);
    }

    @Test
    public void testReturnString_SingleCharacter() {
        String original = "A";
        String copy = new Answer().returnString(original);
        assertEquals(original, copy);
    }

    @Test
    public void testReturnString_NullPointer() {
        assertThrows(IllegalArgumentException.class, () -> {
            new Answer().returnString(null);
        });
    }
}