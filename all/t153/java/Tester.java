package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.*;

import java.nio.ByteBuffer;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import static org.real.temp.Answer.*;
public class Tester {

    /**
     * Utility method to create SHA-256 hash from a string.
     */
    private ByteBuffer createHash(String input) throws NoSuchAlgorithmException {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        byte[] hash = digest.digest(input.getBytes());
        return ByteBuffer.wrap(hash);
    }

    @Test
    public void testShouldReturnStringOfLength5() throws NoSuchAlgorithmException {
        ByteBuffer hash = createHash("test");
        String result = compressHash(hash);
        assertEquals(5, result.length());
    }

    @Test
    public void testShouldReturnDifferentStringsForDifferentInputs() throws NoSuchAlgorithmException {
        ByteBuffer hash1 = createHash("test1");
        ByteBuffer hash2 = createHash("test2");
        String result1 = compressHash(hash1);
        String result2 = compressHash(hash2);
        assertNotEquals(result1, result2);
    }

    @Test
    public void testShouldReturnConsistentResultForSameInput() throws NoSuchAlgorithmException {
        ByteBuffer hash = createHash("test");
        String result1 = compressHash(hash);
        String result2 = compressHash(hash);
        assertEquals(result1, result2);
    }

    @Test
    public void testShouldHandleHashOfAllZeros() {
        ByteBuffer hash = ByteBuffer.allocate(32).put(new byte[32]);
        String result = compressHash(hash);
        assertTrue(result.matches("^[0-9a-zA-Z]{5}$"));
    }

    @Test
    public void testShouldHandleHashOfAllOnes() {
        ByteBuffer hash = ByteBuffer.allocate(32).put(new byte[32]); // 32 bytes of 0xFF
        for (int i = 0; i < 32; i++) {
            hash.put(i, (byte) 0xFF);
        }
        String result = compressHash(hash);
        assertTrue(result.matches("^[0-9a-zA-Z]{5}$"));
    }
}