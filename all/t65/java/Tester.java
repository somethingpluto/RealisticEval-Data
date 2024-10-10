package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Arrays;
import java.util.List;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Tester {

    private DuplicateIpFinder duplicateIpFinder;

    @BeforeEach
    public void setUp() {
        duplicateIpFinder = new DuplicateIpFinder();
    }

    @Test
    public void testFindDuplicateIps() {
        List<String> ipList = Arrays.asList("192.168.1.1", "10.0.0.1", "192.168.1.1", "172.16.0.1");
        List<String> ignoreList = Arrays.asList("10.0.0.1");

        List<String> result = duplicateIpFinder.findDuplicateIps(ipList, ignoreList);

        assertEquals(1, result.size());
        assertTrue(result.contains("192.168.1.1"));
    }
}

class DuplicateIpFinder {

    /**
     * Find duplicate IPs in the given IP list excluding specified IPs to ignore.
     *
     * @param ipList    List of IP addresses
     * @param ignoreList List of IP addresses to ignore
     * @return A list of duplicate IPs excluding those in the ignore list.
     */
    public List<String> findDuplicateIps(List<String> ipList, List<String> ignoreList) {
        // Implementation goes here
        return null; // Placeholder return value
    }
}