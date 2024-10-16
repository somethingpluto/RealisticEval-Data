package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testValidKebabCase() {
        assertTrue(isKebabCase("kebab-case"));
    }

    @Test
    public void testValidKebabCaseWithMultipleWords() {
        assertTrue(isKebabCase("this-is-a-valid-kebab-case"));
    }

    @Test
    public void testUppercaseLetters() {
        assertFalse(isKebabCase("Kebab-Case"));
    }

    @Test
    public void testConsecutiveHyphens() {
        assertFalse(isKebabCase("kebab--case"));
    }

    @Test
    public void testEmptyString() {
        assertFalse(isKebabCase(""));
    }
}