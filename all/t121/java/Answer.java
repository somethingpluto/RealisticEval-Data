package org.real.temp;

import java.util.Arrays;

public class Answer {
    public static int[] adjustArrayLength(int targetLength, int[] array) {
        int arrayLength = array.length;

        if (arrayLength == targetLength) {
            return array;
        }

        if (arrayLength < targetLength) {
            int[] repeatedArray = new int[targetLength];
            for (int i = 0; i < targetLength; i++) {
                repeatedArray[i] = array[i % arrayLength];
            }
            return repeatedArray;
        }

        return Arrays.copyOf(array, targetLength);
    }
}