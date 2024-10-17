package org.real.temp;

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.IOException;

public class Answer {

    /**
     * Retrieve the local IP address of the specified network interface on Windows.
     *
     * @param interfaceName The name of the network interface to check (default is "Wi-Fi").
     * @return The local IP address if found, otherwise null.
     */
    public static String getLocalIp(String interfaceName) {
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

    public static void main(String[] args) {
        String localIp = getLocalIp("Wi-Fi");
        System.out.println("Local IP: " + localIp);
    }
}