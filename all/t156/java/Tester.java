package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testFormatNumber_Million() {
        assertEquals("1.5M", formatNumber(1500000));
        assertEquals("1.0M", formatNumber(1000000));
    }

    @Test
    public void testFormatNumber_Thousand() {
        assertEquals("2.5K", formatNumber(2500));
        assertEquals("1.0K", formatNumber(1000));
    }

    @Test
    public void testFormatNumber_LessThanThousand() {
        assertEquals("999", formatNumber(999));
        assertEquals("500", formatNumber(500));
    }

    @Test
    public void testFormatNumber_EdgeCases() {
        assertEquals("1.0K", formatNumber(1000));
        assertEquals("1.0M", formatNumber(1000000));
    }

    // Assuming the formatNumber method is in this class or imported from elsewhere
    public static String formatNumber(double num) {
        if (num >= 1_000_000) {
            return String.format("%.1fM", num / 1_000_000);
        } else if (num >= 1_000) {
            return String.format("%.1fK", num / 1_000);
        } else {
            return String.valueOf(num);
        }
    }
}