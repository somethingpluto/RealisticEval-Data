package org.real.temp;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Answer {

    /**
     * Find duplicate IPs in the given IP list excluding specified IPs to ignore.
     *
     * @param ipList      List of IP addresses (strings).
     * @param ignoreList  List of IP addresses to ignore (strings).
     * @return A list of duplicate IPs excluding those in the ignore list.
     */
    public static List<String> findDuplicateIps(List<String> ipList, List<String> ignoreList) {
        // Convert ignoreList to a set for faster lookups
        Set<String> ignoreSet = Set.of(ignoreList.toArray(new String[0]));

        // Map to count occurrences of each IP
        Map<String, Integer> ipCount = new HashMap<>();

        // Count occurrences of each IP, excluding ignored IPs
        for (String ip : ipList) {
            if (!ignoreSet.contains(ip)) {
                ipCount.put(ip, ipCount.getOrDefault(ip, 0) + 1);
            }
        }

        // Collect duplicate IPs
        List<String> duplicates = new ArrayList<>();
        for (Map.Entry<String, Integer> entry : ipCount.entrySet()) {
            if (entry.getValue() > 1) {
                duplicates.add(entry.getKey());
            }
        }

        return duplicates;
    }

    // Example usage
    public static void main(String[] args) {
        List<String> ipList = List.of("192.168.1.1", "192.168.1.2", "192.168.1.1", "192.168.1.3");
        List<String> ignoreList = List.of("192.168.1.2");
        List<String> duplicates = findDuplicateIps(ipList, ignoreList);
        System.out.println(duplicates); // Output: [192.168.1.1]
    }
}