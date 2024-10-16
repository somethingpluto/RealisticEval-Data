package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;

public class Tester {

    @Test
    public void testRemoveExistingParameter() throws Exception {
        String url = "https://example.com?page=1&sort=asc&filter=red";
        String result = UrlUtils.removeQueryParam(url, "sort");
        assertEquals("https://example.com/?page=1&filter=red", result);
    }

    @Test
    public void testNoModificationIfParameterDoesNotExist() throws Exception {
        String url = "https://example.com?page=1&filter=red";
        String result = UrlUtils.removeQueryParam(url, "sort");
        assertEquals("https://example.com/?page=1&filter=red", result);
    }

    @Test
    public void testReturnOriginalUrlIfNoQueryParameters() throws Exception {
        String url = "https://example.com";
        String result = UrlUtils.removeQueryParam(url, "sort");
        assertEquals("https://example.com/", result);
    }

    @Test
    public void testRemoveMultipleOccurrencesOfParameter() throws Exception {
        String url = "https://example.com?page=1&filter=red&filter=blue";
        String result = UrlUtils.removeQueryParam(url, "filter");
        assertEquals("https://example.com/?page=1", result);
    }

    @Test
    public void testHandleEncodedCharactersInParameter() throws Exception {
        String url = "https://example.com?page=1&sort=asc&filter=hello%20world";
        String result = UrlUtils.removeQueryParam(url, "filter");
        assertEquals("https://example.com/?page=1&sort=asc", result);
    }

    @Test
    public void testParameterIsOnlyOneInUrl() throws Exception {
        String url = "https://example.com?sort=asc";
        String result = UrlUtils.removeQueryParam(url, "sort");
        assertEquals("https://example.com/", result);
    }
}