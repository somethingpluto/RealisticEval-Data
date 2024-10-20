package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testFirstLetterWhenTargetGreaterThanAll() {
        char[] letters = {'c', 'f', 'j'};
        char target = 'j';
        char result = nextGreatestLetter(letters, target);
        assertEquals('c', result); // Expected output: 'c'
    }

    @Test
    public void testNextGreatestLetterForTypicalInput() {
        char[] letters = {'c', 'f', 'j'};
        char target = 'a';
        char result = nextGreatestLetter(letters, target);
        assertEquals('c', result); // Expected output: 'c'
    }

    @Test
    public void testEdgeCaseWhereTargetInBetween() {
        char[] letters = {'c', 'f', 'j'};
        char target = 'd';
        char result = nextGreatestLetter(letters, target);
        assertEquals('f', result); // Expected output: 'f'
    }

    @Test
    public void testFirstLetterWhenTargetEqualToLargest() {
        char[] letters = {'a', 'b', 'c', 'd'};
        char target = 'd';
        char result = nextGreatestLetter(letters, target);
        assertEquals('a', result); // Expected output: 'a'
    }

    @Test
    public void testCorrectLetterWithSingleElementArray() {
        char[] letters = {'a'};
        char target = 'z';
        char result = nextGreatestLetter(letters, target);
        assertEquals('a', result); // Expected output: 'a'
    }
}