package org.real.temp;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
import org.junit.Test;

public class Tester {

    @Test
    public void testShuffleStringLength() {
        String input = "abcdef";
        String result = shuffleString(input);
        assertEquals(input.length(), result.length());
    }

    @Test
    public void testShuffleStringCharacters() {
        String input = "hello";
        String result = shuffleString(input);
        assertNotEquals(input, result); // It should be different most of the time
    }

    @Test
    public void testShuffleStringEmpty() {
        String input = "";
        String result = shuffleString(input);
        assertEquals("", result); // Should return an empty string
    }

    @Test
    public void testShuffleStringSingleCharacter() {
        String input = "a";
        String result = shuffleString(input);
        assertEquals("a", result); // Should return the same single character
    }

    @Test
    public void testShuffleStringIdenticalCharacters() {
        String input = "aaaaa";
        String result = shuffleString(input);
        assertEquals("aaaaa", result); // Should return the same string
    }

    @Test
    public void testShuffleStringLongerString() {
        String input = "abcdefghijklmnopqrstuvwxyz";
        String result = shuffleString(input);
        assertNotEquals(input, result); // It should be different most of the time
        assertEquals(input.length(), result.length()); // Length should be the same
    }

    @Test
    public void testShuffleStringSameCharacters() {
        String input = "111111";
        String result = shuffleString(input);
        assertEquals("111111", result); // Should return the same string
    }

    @Test
    public void testShuffleStringSpecialCharacters() {
        String input = "a!@#$%^&*()_+";
        String result = shuffleString(input);
        assertEquals(input.length(), result.length()); // Length should be the same
        assertNotEquals(input, result); // It should be different most of the time
    }
}