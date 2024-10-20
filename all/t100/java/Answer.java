package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;

public class Tester {

    @Test
    public void testConvertTimeFullDuration() {
        assertEquals("1h23m45s678ms", convertTime("PT1H23M45.678S"));
    }

    @Test
    public void testConvertTimeOnlySecondsAndMilliseconds() {
        assertEquals("45s500ms", convertTime("PT45.5S"));
    }

    @Test
    public void testConvertTimeHoursAndMinutesNoSeconds() {
        assertEquals("2h5m", convertTime("PT2H5M"));
    }

    @Test
    public void testConvertTimeOnlySecondsNoMilliseconds() {
        assertEquals("20s", convertTime("PT20S"));
    }
}