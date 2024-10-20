package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;

import java.util.Arrays;
import java.util.List;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testBasicDuplicates() {
        List<String> ipList = Arrays.asList("192.168.1.1", "192.168.1.2", "192.168.1.1");
        List<String> ignoreList = Arrays.asList();
        assertEquals(Arrays.asList("192.168.1.1"), findDuplicateIps(ipList, ignoreList));
    }

    @Test
    public void testIgnoredDuplicates() {
        List<String> ipList = Arrays.asList("192.168.1.1", "192.168.1.1", "192.168.1.2");
        List<String> ignoreList = Arrays.asList("192.168.1.1");
        assertEquals(Arrays.asList(), findDuplicateIps(ipList, ignoreList));
    }

    @Test
    public void testNoDuplicates() {
        List<String> ipList = Arrays.asList("192.168.1.1", "192.168.1.2", "192.168.1.3");
        List<String> ignoreList = Arrays.asList();
        assertEquals(Arrays.asList(), findDuplicateIps(ipList, ignoreList));
    }

    @Test
    public void testMixedDuplicates() {
        List<String> ipList = Arrays.asList("192.168.1.1", "192.168.1.1", "10.0.0.1", "192.168.1.2");
        List<String> ignoreList = Arrays.asList("192.168.1.2");
        assertEquals(Arrays.asList("192.168.1.1"), findDuplicateIps(ipList, ignoreList));
    }

    @Test
    public void testEmptyInput() {
        List<String> ipList = Arrays.asList();
        List<String> ignoreList = Arrays.asList();
        assertEquals(Arrays.asList(), findDuplicateIps(ipList, ignoreList));
    }

    @Test
    public void testOnlyIgnoredIPs() {
        List<String> ipList = Arrays.asList("192.168.1.1", "192.168.1.1");
        List<String> ignoreList = Arrays.asList("192.168.1.1");
        assertEquals(Arrays.asList(), findDuplicateIps(ipList, ignoreList));
    }

    @Test
    public void testAllDuplicates() {
        List<String> ipList = Arrays.asList("192.168.1.1", "192.168.1.1", "192.168.1.1");
        List<String> ignoreList = Arrays.asList();
        assertEquals(Arrays.asList("192.168.1.1"), findDuplicateIps(ipList, ignoreList));
    }
}