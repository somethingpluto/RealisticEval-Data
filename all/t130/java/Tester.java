package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testComputePiTo5DecimalPlaces() {
        int digits = 5;
        String expected = "3.14159";
        String result = PiCalculator.computePi(digits);
        assertEquals(expected, result);
    }

    @Test
    public void testComputePiTo10DecimalPlaces() {
        int digits = 10;
        String expected = "3.1415926536";
        String result = PiCalculator.computePi(digits);
        assertEquals(expected, result);
    }

    @Test
    public void testComputePiTo15DecimalPlaces() {
        int digits = 15;
        String expected = "3.141592653589793";
        String result = PiCalculator.computePi(digits);
        assertEquals(expected, result);
    }

    @Test
    public void testComputePiTo20DecimalPlaces() {
        int digits = 20;
        String expected = "3.14159265358979323846";
        String result = PiCalculator.computePi(digits);
        assertEquals(expected, result);
    }

    @Test
    public void testComputePiTo30DecimalPlaces() {
        int digits = 30;
        String expected = "3.141592653589793238462643383280";
        String result = PiCalculator.computePi(digits);
        assertEquals(expected, result);
    }
}