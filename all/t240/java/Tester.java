package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.time.Duration;
import java.util.regex.Pattern;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Tester {

    private Pattern pattern;

    @BeforeEach
    public void setUp() {
        // Define the regex pattern to match the time string format
        pattern = Pattern.compile("(\\d+)d(\\d+)h(\\d+)m(\\d+)s(\\d+)ms");
    }

    @Test
    public void testGenTimeoutTimedelta() {
        String timeString = "1d 2h 3m 4s 500ms";
        Duration expectedDuration = Duration.ofDays(1).plusHours(2).plusMinutes(3).plusSeconds(4).plusMillis(500);
        Duration actualDuration = genTimeoutTimedelta(timeString);

        assertEquals(expectedDuration.toDays(), actualDuration.toDays());
        assertEquals(expectedDuration.toHoursPart(), actualDuration.toHoursPart());
        assertEquals(expectedDuration.toMinutesPart(), actualDuration.toMinutesPart());
        assertEquals(expectedDuration.getSeconds(), actualDuration.getSeconds());
        assertEquals(expectedDuration.getNano() / 1_000_000, actualDuration.getNano() / 1_000_000);
    }

    @Test
    public void testInvalidTimeFormat() {
        String invalidTimeString = "1d 2h 3m 4s 500"; // Missing 'ms' at the end

        assertThrows(IllegalArgumentException.class, () -> {
            genTimeoutTimedelta(invalidTimeString);
        });
    }

    @Test
    public void testEmptyTimeFormat() {
        String emptyTimeString = "";

        assertThrows(IllegalArgumentException.class, () -> {
            genTimeoutTimedelta(emptyTimeString);
        });
    }

    private Duration genTimeoutTimedelta(String timeString) {
        if (timeString == null || timeString.isEmpty()) {
            throw new IllegalArgumentException("Input string cannot be null or empty");
        }

        Matcher matcher = pattern.matcher(timeString);
        if (!matcher.matches()) {
            throw new IllegalArgumentException("Invalid time format");
        }

        int days = Integer.parseInt(matcher.group(1));
        int hours = Integer.parseInt(matcher.group(2));
        int minutes = Integer.parseInt(matcher.group(3));
        int seconds = Integer.parseInt(matcher.group(4));
        int milliseconds = Integer.parseInt(matcher.group(5));

        return Duration.ofDays(days)
                .plusHours(hours)
                .plusMinutes(minutes)
                .plusSeconds(seconds)
                .plusMillis(milliseconds);
    }
}