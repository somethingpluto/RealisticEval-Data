package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;
import static org.junit.Assert.assertFalse;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void validatesAStandardHttpUrl() {
        String url = "http://www.example.com";
        assertTrue(validURL(url));
    }

    @Test
    public void validatesASecureHttpsUrl() {
        String url = "https://www.example.com";
        assertTrue(validURL(url));
    }

    @Test
    public void rejectsAMalformedUrl() {
        String url = "htp:/www.example.com";
        assertFalse(validURL(url));
    }

}