package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {
    public static List<Object> safeSplice(List<Object> inputArray, int amountToRemove, int indexToRemove, Object replaceWith) {
        List<Object> before = new ArrayList<>(inputArray.subList(0, indexToRemove));
        List<Object> after = new ArrayList<>(inputArray.subList(indexToRemove + amountToRemove, inputArray.size()));

        if (replaceWith != null) {
            before.add(replaceWith);
        }

        before.addAll(after);
        return before;
    }
}