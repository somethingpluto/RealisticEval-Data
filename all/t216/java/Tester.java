package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.InputStream;
import java.io.PrintStream;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertThrows;
import static org.mockito.Mockito.when;

public class Tester {

    @Mock
    private Process processMock;

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @Before
    public void setUp() {
        MockitoAnnotations.initMocks(this); // Use initMocks for JUnit 4
        System.setOut(new PrintStream(outContent));
    }

    @Test
    public void testSuccessfulIpRetrieval() {
        // Sample IP command output for a wlan0 interface
        String sampleOutput = "3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000\n" +
                              "    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic wlan0\n" +
                              "       valid_lft 86394sec preferred_lft 86394sec\n";

        when(processMock.getInputStream()).thenReturn(new ByteArrayInputStream(sampleOutput.getBytes()));
        when(processMock.exitValue()).thenReturn(0);

        String ip = getLocalIp("wlan0");
        assertEquals("192.168.1.100", ip);
    }

    @Test
    public void testCommandFailure() {
        when(processMock.exitValue()).thenReturn(1);

        // Adjusting the assertThrows to match JUnit 4 syntax
        try {
            getLocalIp("wlan0");
        } catch (RuntimeException e) {
            // Assert that we caught a RuntimeException
            return;
        }
        // If we did not throw an exception, fail the test
        throw new AssertionError("Expected RuntimeException was not thrown");
    }

    @Test
    public void testDifferentInterface() {
        // Sample IP command output for a different interface
        String sampleOutput = "3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500\n" +
                              "    inet 10.0.0.1/24";

        when(processMock.getInputStream()).thenReturn(new ByteArrayInputStream(sampleOutput.getBytes()));
        when(processMock.exitValue()).thenReturn(0);

        String ip = getLocalIp("eth0");
        assertEquals("10.0.0.1", ip);
    }
}
