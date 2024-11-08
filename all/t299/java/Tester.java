package org.real.temp;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
import org.junit.Test;

public class Tester {

    @Test
    public void testBirthdayToday() {
        assertEquals("2000-08-23 (24)", calculateAge("2000-08-23"));
    }

    @Test
    public void testBirthdayHasPassed() {
        assertEquals("1990-01-15 (34)", calculateAge("1990-01-15"));
    }

    @Test
    public void testBirthdayAtEndOfYear() {
        assertEquals("1985-12-31 (38)", calculateAge("1985-12-31"));
    }

    @Test
    public void testRecentlyTurnedOne() {
        assertEquals("2023-05-05 (1)", calculateAge("2023-05-05"));
    }

    @Test
    public void testInvalidDateInput() {
        assertEquals("", calculateAge("invalid-date"));
    }
}