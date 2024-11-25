package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testSafeFormatWithName() {
        assertEquals("Hello, John!", safeFormat("Hello, {name}!", "John"));
    }

    @Test
    public void testSafeFormatWithAnswer() {
        assertEquals("The answer is {answer}.", safeFormat("The answer is {answer}.", "42"));
    }

    @Test
    public void testSafeFormatWithoutArguments() {
        assertEquals("No replacements here.", safeFormat("No replacements here."));
    }

    @Test
    public void testSafeFormatWithUnchanged() {
        assertEquals("Keep {unchanged} unchanged.", safeFormat("Keep {unchanged} unchanged."));
    }

    @Test
    public void testSafeFormatWithPartialReplacement() {
        assertEquals("Replace {first}, keep {second}.", safeFormat("Replace {first}, keep {second}.", "first"));
    }


}
