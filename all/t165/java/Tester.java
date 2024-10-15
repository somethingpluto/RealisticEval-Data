package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testBase64ToUrlSafe_ConvertsStandardBase64() {
        String base64 = "YW55IGNhcm5hbCBwbGVhc3VyZS4+/w==";
        String result = Base64Converter.base64ToUrlSafe(base64);
        assertEquals("YW55IGNhcm5hbCBwbGVhc3VyZS4-_w", result);
    }

    @Test
    public void testBase64ToUrlSafe_EmptyString() {
        String base64 = "";
        String result = Base64Converter.base64ToUrlSafe(base64);
        assertEquals("", result);
    }

    @Test
    public void testBase64ToUrlSafe_RemovesTrailingEquals() {
        String base64 = "dGVzdA==";
        String result = Base64Converter.base64ToUrlSafe(base64);
        assertEquals("dGVzdA", result);
    }

    @Test
    public void testBase64ToUrlSafe_NoReplacementNeeded() {
        String base64 = "dGVzdA";
        String result = Base64Converter.base64ToUrlSafe(base64);
        assertEquals("dGVzdA", result);
    }

    @Test
    public void testBase64ToUrlSafe_MultipleCharacters() {
        String base64 = "aGVsbG8rL3dvcmxkLw==";
        String result = Base64Converter.base64ToUrlSafe(base64);
        assertEquals("aGVsbG8rL3dvcmxkLw", result);
    }

    @Test(expected = TypeError.class)
    public void testBase64ToUrlSafe_NonStringInput() {
        Base64Converter.base64ToUrlSafe(null); // Adjust this to your error handling
    }
}