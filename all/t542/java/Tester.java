package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testCalculateDiscount1() {
        assertEquals(25.00, calculateDiscount(100, 75), 0.01);
    }

    @Test
    public void testCalculateDiscount2() {
        assertEquals(0.00, calculateDiscount(50, 50), 0.01);
    }

    @Test
    public void testCalculateDiscount3() {
        assertEquals(100.00, calculateDiscount(100, 0), 0.01);
    }

    @Test
    public void testCalculateDiscount4() {
        assertEquals(50.00, calculateDiscount(200, 100), 0.01);
    }
}