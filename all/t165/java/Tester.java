package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.*;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testBase64ToUrlSafe_ConvertsStandardBase64() {
        String base64 = "YW55IGNhcm5hbCBwbGVhc3VyZS4+/w==";
        String result = base64ToUrlSafe(base64);
        assertEquals("YW55IGNhcm5hbCBwbGVhc3VyZS4-_w", result);
    }

    @Test
    public void testBase64ToUrlSafe_EmptyString() {
        String base64 = "";
        String result = base64ToUrlSafe(base64);
        assertEquals("", result);
    }

    @Test
    public void testBase64ToUrlSafe_RemovesTrailingEquals() {
        String base64 = "dGVzdA==";
        String result = base64ToUrlSafe(base64);
        assertEquals("dGVzdA", result);
    }

    @Test
    public void testBase64ToUrlSafe_NoReplacementNeeded() {
        String base64 = "dGVzdA";
        String result = base64ToUrlSafe(base64);
        assertEquals("dGVzdA", result);
    }

    @Test
    public void testBase64ToUrlSafe_MultipleCharacters() {
        String base64 = "aGVsbG8rL3dvcmxkLw==";
        String result = base64ToUrlSafe(base64);
        assertEquals("aGVsbG8rL3dvcmxkLw", result);
    }

}