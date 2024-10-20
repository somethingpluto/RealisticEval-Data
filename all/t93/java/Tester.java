package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testGetAllAlphabetsLength() {
        char[] result =getAllAlphabets();
        assertEquals(52, result.length);
    }

    @Test
    public void testGetAllAlphabetsLowercase() {
        char[] result =getAllAlphabets();
        char[] lowercaseAlphabets = new char[26];
        System.arraycopy(result, 0, lowercaseAlphabets, 0, 26);

        char[] expected = {
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z'
        };

        assertArrayEquals(expected, lowercaseAlphabets);
    }

    @Test
    public void testGetAllAlphabetsUppercase() {
        char[] result =getAllAlphabets();
        char[] uppercaseAlphabets = new char[26];
        System.arraycopy(result, 26, uppercaseAlphabets, 0, 26);

        char[] expected = {
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                'U', 'V', 'W', 'X', 'Y', 'Z'
        };

        assertArrayEquals(expected, uppercaseAlphabets);
    }

    @Test
    public void testGetAllAlphabetsFirstElement() {
        char[] result =getAllAlphabets();
        assertEquals('a', result[0]);
    }

    @Test
    public void testGetAllAlphabetsLastElement() {
        char[] result =getAllAlphabets();
        assertEquals('Z', result[result.length - 1]);
    }
}