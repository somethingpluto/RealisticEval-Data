package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testAlreadySymmetricMatrix() {
        char[][] matrix = {
            {'a', 'b', 'c'},
            {'b', 'e', 'f'},
            {'c', 'f', 'i'}
        };
        assertEquals(0, Answer.minChangesToSymmetric(matrix));
    }

    @Test
    public void testOneChangeNeeded() {
        char[][] matrix = {
            {'a', 'b', 'c'},
            {'d', 'e', 'f'},
            {'c', 'h', 'i'}
        };
        assertEquals(2, Answer.minChangesToSymmetric(matrix));
    }

    @Test
    public void testAllDifferentElements() {
        char[][] matrix = {
            {'a', 'b', 'c'},
            {'d', 'e', 'f'},
            {'g', 'h', 'i'}
        };
        assertEquals(3, Answer.minChangesToSymmetric(matrix));
    }

    @Test
    public void testLargeSymmetricMatrix() {
        char[][] matrix = {
            {'a', 'b', 'c', 'd'},
            {'b', 'e', 'f', 'g'},
            {'c', 'f', 'h', 'i'},
            {'d', 'g', 'i', 'j'}
        };
        assertEquals(0, Answer.minChangesToSymmetric(matrix));
    }

    @Test
    public void testMultipleChangesNeeded() {
        char[][] matrix = {
            {'a', 'x', 'c', 'd'},
            {'y', 'e', 'f', 'g'},
            {'z', 'h', 'i', 'j'},
            {'d', 'g', 'k', 'l'}
        };
        assertEquals(4, Answer.minChangesToSymmetric(matrix));
    }
}