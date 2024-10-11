package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

public class TestDecryptFunction {

    @Test
    public void testBasicFunctionality() {
        assertEquals(new int[]{4, 4, 4, 4}, performPolynomialDecryption(4, 5, new int[]{1, 2, 3, 4}, new int[]{5, 6, 7, 8}));
    }

    @Test
    public void testZeroSecretKey() {
        assertEquals(new int[]{6, 6, 6}, performPolynomialDecryption(3, 7, new int[]{0, 0, 0}, new int[]{6, 13, 20}));
    }

    @Test
    public void testZeroCiphertext() {
        assertEquals(new int[]{8, 7, 6}, performPolynomialDecryption(3, 9, new int[]{1, 2, 3}, new int[]{0, 0, 0}));
    }

    @Test
    public void testLargeValues() {
        assertEquals(new int[]{500, 500}, performPolynomialDecryption(2, 1000, new int[]{500, 500}, new int[]{1000, 1000}));
    }
}
