package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.util.HashMap;
import java.util.Map;

public class Tester {

    @Test
    public void testToQueryString_SimpleObject() {
        Map<String, Object> params = new HashMap<>();
        params.put("search", "test");
        params.put("page", 1);
        params.put("size", 10);

        String result = QueryStringConverter.toQueryString(params);
        assertEquals("?search=test&page=1&size=10", result);
    }

    @Test
    public void testToQueryString_EncodeSpecialCharacters() {
        Map<String, Object> params = new HashMap<>();
        params.put("search", "hello world");
        params.put("filter", "price < $50");

        String result = QueryStringConverter.toQueryString(params);
        assertEquals("?search=hello%20world&filter=price%20%3C%20%2450", result);
    }

    @Test
    public void testToQueryString_HandleEmptyStringValues() {
        Map<String, Object> params = new HashMap<>();
        params.put("search", "");
        params.put("page", 1);

        String result = QueryStringConverter.toQueryString(params);
        assertEquals("?search=&page=1", result);
    }

    @Test
    public void testToQueryString_HandleBooleanValues() {
        Map<String, Object> params = new HashMap<>();
        params.put("isActive", true);
        params.put("isVerified", false);

        String result = QueryStringConverter.toQueryString(params);
        assertEquals("?isActive=true&isVerified=false", result);
    }
}