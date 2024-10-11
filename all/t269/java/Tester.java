package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class TesterTest {

    @Test
    public void testIsCompliantIpValid() {
        assertTrue(Tester.isCompliantIp("192.168.1.1"));
    }

    @Test
    public void testIsCompliantIpInvalid() {
        assertFalse(Tester.isCompliantIp("256.256.256.256"));
    }

    @Test
    public void testIsCompliantIpEmptyString() {
        assertFalse(Tester.isCompliantIp(""));
    }

    @Test
    public void testIsCompliantIpNull() {
        assertThrows(NullPointerException.class, () -> Tester.isCompliantIp(null));
    }

    @Test
    public void testIsCompliantIpIncorrectFormat() {
        assertFalse(Tester.isCompliantIp("192.168.1"));
        assertFalse(Tester.isCompliantIp("192.168.1.a"));
    }
}