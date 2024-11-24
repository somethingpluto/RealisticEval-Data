package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testDecimalScore() {
        // Test a simple decimal score.
        assertEquals(2.5, convertScoreToDecimal("2.5"), 0.001);
    }

    @Test
    public void testFractionScore() {
        // Test a fraction score.
        assertEquals(2.5, convertScoreToDecimal("10/4"), 0.001);
    }

    @Test
    public void testIntegerScore() {
        // Test an integer score represented as a string.
        assertEquals(5.0, convertScoreToDecimal("5"), 0.001);
    }

    @Test
    public void testIntegerDivideScore() {
        // Test an integer division score.
        assertEquals(4.0, convertScoreToDecimal("12/3"), 0.001);
    }
}