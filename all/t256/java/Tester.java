package org.real.temp;
import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;
import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {


    @Test
    public void testExactMultipleOfEight() {
        List<Integer> bits = Arrays.asList(1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1);
        byte[] expected = new byte[]{(byte) 0b10110010, 0b01001111};
        byte[] result = bitsToBytes(bits);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testIncompleteByteDiscarded() {
        List<Integer> bits = Arrays.asList(1, 0, 1, 1, 0, 0, 1, 0, 0, 1);
        byte[] expected = new byte[]{(byte) 0b10110010};
        byte[] result = bitsToBytes(bits);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testEmptyBitArray() {
        List<Integer> bits = Arrays.asList();
        byte[] expected = new byte[]{};
        byte[] result = bitsToBytes(bits);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testSingleFullByte() {
        List<Integer> bits = Arrays.asList(1, 1, 1, 1, 1, 1, 1, 1);
        byte[] expected = new byte[]{(byte) 0xFF};
        byte[] result = bitsToBytes(bits);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testNoBitsDiscarded() {
        List<Integer> bits = Arrays.asList(1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1);
        byte[] expected = new byte[]{(byte) 0xCC, 0x77};
        byte[] result = bitsToBytes(bits);
        assertArrayEquals(expected, result);
    }
}