package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testCountConsecutiveLettersCorrectly() {
        List<Integer> result = countLetterChanges("aaabbcdeee");
        assertEquals(Arrays.asList(3, 2, 1, 1, 3), result);
    }

    @Test
    public void testSingleCharacter() {
        List<Integer> result = countLetterChanges("a");
        assertEquals(Arrays.asList(1), result);
    }

    @Test
    public void testNoConsecutiveLetters() {
        List<Integer> result = countLetterChanges("abcdef");
        assertEquals(Arrays.asList(1, 1, 1, 1, 1, 1), result);
    }

    @Test
    public void testIdenticalLetters() {
        List<Integer> result = countLetterChanges("rrrrrr");
        assertEquals(Arrays.asList(6), result);
    }

    @Test
    public void testLongStringWithRandomLetters() {
        List<Integer> result = countLetterChanges("xxxyyyzzzaaaab");
        assertEquals(Arrays.asList(3, 3, 3, 4, 1), result);
    }

    @Test
    public void testNumericCharactersInString() {
        List<Integer> result = countLetterChanges("1122334455");
        assertEquals(Arrays.asList(2, 2, 2, 2, 2), result);
    }
}