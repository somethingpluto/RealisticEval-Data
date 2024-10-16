package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testHideBankAccountValidCases() {
        assertEquals("****4567", BankAccountHider.hideBankAccount("12345678901234567"));
        assertEquals("****6543", BankAccountHider.hideBankAccount("98765432109876543"));
        assertEquals("****1100", BankAccountHider.hideBankAccount("11111111111111100"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void testHideBankAccountShorterThan17Characters() {
        BankAccountHider.hideBankAccount("1234567890123456");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testHideBankAccountLongerThan17Characters() {
        BankAccountHider.hideBankAccount("123456789012345678");
    }

    @Test(expected = IllegalArgumentException.class)
    public void testHideBankAccountWithZeroCharacters() {
        BankAccountHider.hideBankAccount("");
    }
}