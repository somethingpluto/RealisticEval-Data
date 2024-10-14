package org.real.temp;

public class Answer {
    public static boolean isValidPortNumber(int port) {
        if (port < 1 || port > 65535) {
            return false;
        }
        return true;
    }
    
    public static void main(String[] args) {
        // Example usage
        try {
            int port = 8080; // Example port
            System.out.println("Is valid port: " + isValidPortNumber(port));
        } catch (IllegalArgumentException e) {
            System.err.println(e.getMessage());
        }
    }
}