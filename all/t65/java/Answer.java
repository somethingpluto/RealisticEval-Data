package org.real.temp;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class Answer {

    public static List<String> findDuplicateIps(List<String> ipList, List<String> ignoreList) {
        Set<String> uniqueIpSet = new HashSet<>();
        Set<String> duplicateIpSet = new HashSet<>();

        for(String ip : ipList){
            if(!ignoreList.contains(ip)){
                if(uniqueIpSet.contains(ip)){
                    duplicateIpSet.add(ip);
                } else {
                    uniqueIpSet.add(ip);
                }
            }
        }

        return new ArrayList<>(duplicateIpSet);
    }
}