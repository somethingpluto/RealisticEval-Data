package org.real.temp;

import org.junit.Test;
import java.util.Map;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

public class Tester {

    @Test
    public void testValidPostRequestLine() {
        String response = "POST /api/data HTTP/1.1\r\n";
        Map<String, String> parsedInfo = Answer.parseHttpRequestLine(response);

        assertEquals("POST", parsedInfo.get("method"));
        assertEquals("/api/data", parsedInfo.get("url"));
        assertEquals("HTTP/1.1", parsedInfo.get("http_version"));
    }

    @Test
    public void testPutRequestLine() {
        String response = "PUT /api/update HTTP/2.0\r\n";
        Map<String, String> parsedInfo = Answer.parseHttpRequestLine(response);

        assertEquals("PUT", parsedInfo.get("method"));
        assertEquals("/api/update", parsedInfo.get("url"));
        assertEquals("HTTP/2.0", parsedInfo.get("http_version"));
    }

    @Test
    public void testDeleteRequestLine() {
        String response = "DELETE /api/delete HTTP/1.1\r\n";
        Map<String, String> parsedInfo = Answer.parseHttpRequestLine(response);

        assertEquals("DELETE", parsedInfo.get("method"));
        assertEquals("/api/delete", parsedInfo.get("url"));
        assertEquals("HTTP/1.1", parsedInfo.get("http_version"));
    }

    @Test
    public void testMalformedRequestLine() {
        String response = "INVALID REQUEST LINE\r\n";
        Map<String, String> parsedInfo = Answer.parseHttpRequestLine(response);

        assertTrue(parsedInfo.isEmpty());  // Expect empty result for malformed request
    }
}