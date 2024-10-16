package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void shouldReturnTrueForValidPascalCaseString() {
        assertTrue(isPascalCase("PascalCase"));
    }

    @Test
    public void shouldReturnTrueForValidPascalCaseStringWithMultipleWords() {
        assertTrue(isPascalCase("PascalCaseExample"));
    }

    @Test
    public void shouldReturnFalseForStringThatStartsWithLowercaseLetter() {
        assertFalse(isPascalCase("pascalCase"));
    }

    @Test
    public void shouldReturnFalseForStringWithUnderscores() {
        assertFalse(isPascalCase("Pascal_case"));
    }

    @Test
    public void shouldReturnFalseForEmptyString() {
        assertFalse(isPascalCase(""));
    }
}