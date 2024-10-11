package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class Tester {

    // Assuming these methods will be implemented with some functionality
    public String red(String text) {
        return "\033[31m" + text + "\033[0m";
    }

    public String green(String text) {
        return "\033[32m" + text + "\033[0m";
    }

    public String blue(String text) {
        return "\033[34m" + text + "\033[0m";
    }

    public String yellow(String text) {
        return "\033[33m" + text + "\033[0m";
    }

    public String magenta(String text) {
        return "\033[35m" + text + "\033[0m";
    }

    public String cyan(String text) {
        return "\033[36m" + text + "\033[0m";
    }

    @Test
    public void testRed() {
        assertEquals("\033[31mHello\033[0m", red("Hello"));
    }

    @Test
    public void testGreen() {
        assertEquals("\033[32mHello\033[0m", green("Hello"));
    }

    @Test
    public void testBlue() {
        assertEquals("\033[34mHello\033[0m", blue("Hello"));
    }

    @Test
    public void testYellow() {
        assertEquals("\033[33mHello\033[0m", yellow("Hello"));
    }

    @Test
    public void testMagenta() {
        assertEquals("\033[35mHello\033[0m", magenta("Hello"));
    }

    @Test
    public void testCyan() {
        assertEquals("\033[36mHello\033[0m", cyan("Hello"));
    }
}