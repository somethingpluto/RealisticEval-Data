package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class Tester {

    @Test
    public void testCalculateFinalPriceWithValidInputs() {
        double result = PriceCalculator.calculateFinalPrice("200", "10");
        assertEquals(180.0, result, 0.01);
    }

    @Test
    public void testCalculateFinalPriceWithZeroDiscount() {
        double result = PriceCalculator.calculateFinalPrice("150", "0");
        assertEquals(150.0, result, 0.01);
    }

    @Test
    public void testCalculateFinalPriceWithHundredPercentDiscount() {
        double result = PriceCalculator.calculateFinalPrice("100", "100");
        assertEquals(0.0, result, 0.01);
    }
}