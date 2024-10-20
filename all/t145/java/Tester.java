package org.real.temp;

import static org.junit.Assert.assertEquals;

import org.junit.Test;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testFormatCurrencyInUSD() {
        double value = 1234.56;
        String currencyCode = "USD";
        String locale = "en-US";
        String expectedOutput = "$1,234.56"; // Expected format for USD
        assertEquals(expectedOutput, formatCurrency(value, currencyCode, locale));
    }

    @Test
    public void testFormatCurrencyInEuro() {
        double value = 1234.56;
        String currencyCode = "EUR";
        String locale = "en-US";
        String expectedOutput = "€1,234.56"; // Expected format for EUR
        assertEquals(expectedOutput, formatCurrency(value, currencyCode, locale));
    }

    @Test
    public void testFormatCurrencyInBritishPound() {
        double value = 1234.56;
        String currencyCode = "GBP";
        String locale = "en-GB";
        String expectedOutput = "£1,234.56"; // Expected format for GBP
        assertEquals(expectedOutput, formatCurrency(value, currencyCode, locale));
    }

    @Test
    public void testFormatCurrencyNegativeValue() {
        double value = -1234.56;
        String currencyCode = "USD";
        String locale = "en-US";
        String expectedOutput = "-$1,234.56"; // Expected format for negative USD
        assertEquals(expectedOutput, formatCurrency(value, currencyCode, locale));
    }

    @Test
    public void testHandleZeroValueCorrectly() {
        double value = 0;
        String currencyCode = "JPY";
        String locale = "en-JP";
        String expectedOutput = "¥0"; // Expected format for JPY (no decimals)
        assertEquals(expectedOutput, formatCurrency(value, currencyCode, locale));
    }
}