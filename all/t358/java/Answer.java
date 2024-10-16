package org.real.temp;

import java.util.Arrays;
import java.util.Comparator;

/**
 * @brief Sort the string array with the shape of "name + number" in ascending order.
 * If the numbers are the same, sort by name in ascending order, and return the sorted array.
 *
 * @param arr An array of strings to be sorted.
 * @return An array of strings sorted according to the rules described above.
 */
public class Answer {
    public static String[] sortNames(String[] arr) {
        Arrays.sort(arr, new Comparator<String>() {
            @Override
            public int compare(String a, String b) {
                String[] nameAndNumberA = extractNameAndNumber(a);
                String[] nameAndNumberB = extractNameAndNumber(b);
                int numberA = Integer.parseInt(nameAndNumberA[1]);
                int numberB = Integer.parseInt(nameAndNumberB[1]);

                if (numberA != numberB) {
                    return Integer.compare(numberA, numberB);
                }
                return nameAndNumberA[0].compareTo(nameAndNumberB[0]);
            }
        });
        return arr;
    }

    private static String[] extractNameAndNumber(String s) {
        int pos = s.length() - 1;
        while (pos >= 0 && Character.isDigit(s.charAt(pos))) {
            pos--;
        }
        String name = s.substring(0, pos + 1).trim();
        String number = s.substring(pos + 1).trim();
        return new String[]{name, number};
    }
}