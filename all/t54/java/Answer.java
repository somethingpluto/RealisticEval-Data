package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static List<String> removeTripleBackticks(List<String> stringList) {
        List<String> resultList = new ArrayList<>();

        for(String str : stringList) {
            String resultStr = str.replaceAll("```", "");
            resultList.add(resultStr);
        }

        return resultList;
    }
}