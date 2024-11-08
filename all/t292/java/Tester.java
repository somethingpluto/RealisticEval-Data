package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
import org.junit.Test;

public class Tester {

    @Test
    public void testCalculateRemainingPaymentTypicalLoan() {
        assertEquals(0, calculateRemainingPayment(10000, 0.005, 24), 0.01);
    }

    @Test
    public void testCalculateRemainingPaymentHighInterest() {
        assertEquals(0, calculateRemainingPayment(10000, 0.1, 12), 0.01);
    }

    @Test
    public void testCalculateRemainingPaymentLowInterest() {
        assertEquals(0, calculateRemainingPayment(10000, 0.001, 60), 0.01);
    }

    @Test
    public void testCalculateRemainingPaymentVeryShortTerm() {
        assertEquals(0, calculateRemainingPayment(10000, 0.005, 1), 0.01);
    }

    @Test
    public void testCalculateRemainingPaymentNoPayments() {
        assertEquals(10000, calculateRemainingPayment(10000, 0.005, 0), 0.01);
    }

    @Test
    public void testCalculateRemainingPaymentLongTerm() {
        assertEquals(0, calculateRemainingPayment(10000, 0.005, 360), 0.01);
    }
}