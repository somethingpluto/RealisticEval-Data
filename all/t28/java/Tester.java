package org.real.temp;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.io.TempDir;
import java.io.ByteArrayOutputStream;
import java.io.PrintStream;

import static org.junit.jupiter.api.Assertions.assertEquals;

/**
 * Test class for verifying the correctness of the printMemoryBits method.
 */
public class Tester {

    private final ByteArrayOutputStream outContent = new ByteArrayOutputStream();

    @BeforeEach
    public void setUp() {
        // Redirect System.out to capture the output
        System.setOut(new PrintStream(outContent));
    }

    @AfterEach
    public void tearDown() {
        // Restore the normal System.out
        System.setOut(System.out);
    }

    @Test
    public void testSingleByte() {
        byte[] memorySection = new byte[]{(byte) 0b10101010};
        printMemoryBits(memorySection);
        String output = outContent.toString().trim();
        String expectedOutput = "10101010";
        assertEquals(expectedOutput, output);
    }

    @Test
    public void testMultipleBytes() {
        byte[] memorySection = new byte[]{(byte) 0b11001100, (byte) 0b11110000};
        printMemoryBits(memorySection);
        String output = outContent.toString().trim();
        String expectedOutput = "11001100\n11110000";
        assertEquals(expectedOutput, output);
    }

    @Test
    public void testAllZeros() {
        byte[] memorySection = new byte[]{(byte) 0b00000000};
        printMemoryBits(memorySection);
        String output = outContent.toString().trim();
        String expectedOutput = "00000000";
        assertEquals(expectedOutput, output);
    }

    @Test
    public void testAllOnes() {
        byte[] memorySection = new byte[]{(byte) 0b11111111};
        printMemoryBits(memorySection);
        String output = outContent.toString().trim();
        String expectedOutput = "11111111";
        assertEquals(expectedOutput, output);
    }
}