package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static List<Object> flattenArray(List<?> multiDimArray) {
        List<Object> flatList = new ArrayList<>();

        for(Object obj : multiDimArray) {
            if(obj instanceof List<?>) {
                flatList.addAll(flattenArray((List<?>)obj));
            } else {
                flatList.add(obj);
            }
        }

        return flatList;
    }
}