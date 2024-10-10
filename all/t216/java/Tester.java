package org.real.temp;

import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TestTester {

    @Test
    public void testGetLocalIp() {
        String expectedIp = "192.168.1.1"; // Replace with the expected IP address
        String actualIp = Tester.getLocalIp("wlan0");
        
        assertEquals(expectedIp, actualIp);
    }
}