package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testConvertTimeFullDuration() {
        assertEquals("1h23m45s678ms", TimeConverter.convertTime("PT1H23M45.678S"));
    }

    @Test
    public void testConvertTimeOnlySecondsAndMilliseconds() {
        assertEquals("45s500ms", TimeConverter.convertTime("PT45.5S"));
    }

    @Test
    public void testConvertTimeHoursAndMinutesNoSeconds() {
        assertEquals("2h5m", TimeConverter.convertTime("PT2H5M"));
    }

    @Test
    public void testConvertTimeOnlySecondsNoMilliseconds() {
        assertEquals("20s", TimeConverter.convertTime("PT20S"));
    }
}