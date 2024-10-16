package org.real.temp;

import static org.junit.Assert.*;
import org.junit.Test;

public class Tester {

    @Test
    public void testValidSnakeCase() {
        assertTrue(StringUtil.isSnakeCase("snake_case"));
    }

    @Test
    public void testValidSnakeCaseMultipleWords() {
        assertTrue(StringUtil.isSnakeCase("snake_case_example"));
    }

    @Test
    public void testStartsWithUppercase() {
        assertFalse(StringUtil.isSnakeCase("Snake_Case"));
    }

    @Test
    public void testMixedCaseLetters() {
        assertFalse(StringUtil.isSnakeCase("snakeCASE"));
    }

    @Test
    public void testWithNumbers() {
        assertFalse(StringUtil.isSnakeCase("snake_case_123"));
    }

    @Test
    public void testEmptyString() {
        assertFalse(StringUtil.isSnakeCase(""));
    }
}