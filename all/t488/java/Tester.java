package org.real.temp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.mockito.Mockito.when;
import static org.mockito.Mockito.doThrow;

public class Tester {

    @Mock
    private Process processMock;

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
        System.setOut(new PrintStream(outContent));
    }

    @Test
    public void testLocalIpFound() throws IOException {
        // Mock the output of ipconfig for a case where a local IP is found
        when(Runtime.getRuntime().exec("ipconfig")).thenReturn(processMock);
        when(processMock.getInputStream()).thenReturn(new ByteArrayInputStream("192.168.1.10\n".getBytes()));

        String result = getLocalIp();
        assertEquals("192.168.1.10", result);
    }

    @Test
    public void testNoLocalIpFound() throws IOException {
        // Mock the output of ipconfig for a case where no local IP is found
        when(Runtime.getRuntime().exec("ipconfig")).thenReturn(processMock);
        when(processMock.getInputStream()).thenReturn(new ByteArrayInputStream("10.0.0.5\n".getBytes()));

        String result = getLocalIp();
        assertNull(result);
    }

    @Test
    public void testMultipleIpsFound() throws IOException {
        // Mock the output with multiple local IPs
        when(Runtime.getRuntime().exec("ipconfig")).thenReturn(processMock);
        when(processMock.getInputStream()).thenReturn(new ByteArrayInputStream("10.0.0.5\n192.168.1.10\n".getBytes()));

        String result = getLocalIp();
        assertEquals("192.168.1.10", result);
    }

    @Test
    public void testInvalidCommand() {
        // Simulate a case where subprocess.run raises a CalledProcessError
        doThrow(new IOException("CalledProcessError")).when(Runtime.getRuntime()).exec("ipconfig");

        String result = getLocalIp();
        assertNull(result);
    }

    @Test
    public void testUnexpectedError() {
        // Simulate an unexpected error
        doThrow(new RuntimeException("Unexpected error")).when(Runtime.getRuntime()).exec("ipconfig");

        String result = getLocalIp();
        assertNull(result);
    }

    // Utility method to simulate the getLocalIp method
    private String getLocalIp() {
        try {
            // Execute the 'ipconfig' command to get addresses for the specified interface
            Process process = Runtime.getRuntime().exec("ipconfig");
            StringBuilder output = new StringBuilder();
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));

            String line;
            while ((line = reader.readLine()) != null) {
                output.append(line).append("\n");
            }

            // Regular expression to match IPv4 addresses
            Pattern ipPattern = Pattern.compile("(\\d+\\.\\d+\\.\\d+\\.\\d+)");

            // Search for IP addresses in the command output
            Matcher matcher = ipPattern.matcher(output.toString());
            while (matcher.find()) {
                String ip = matcher.group(1);
                if (ip.startsWith("192.168.")) {
                    return ip; // Return the first local IP found
                }
            }

            return null; // Return null if no suitable IP is found

        } catch (IOException e) {
            System.out.println("Error executing command: " + e.getMessage());
            return null;
        } catch (Exception e) {
            System.out.println("An unexpected error occurred: " + e.getMessage());
            return null;
        }
    }
}