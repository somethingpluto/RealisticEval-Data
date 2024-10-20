package org.real.temp;
import java.util.HashSet;
import java.util.Set;

public class Answer {

    public static <T> boolean compareArrays(T[] arr1, T[] arr2) {
        Set<T> set1 = new HashSet<>(Set.of(arr1));
        Set<T> set2 = new HashSet<>(Set.of(arr2));

        if (set1.size() != set2.size()) {
            return false;
        }

        for (T item : set1) {
            if (!set2.contains(item)) {
                return false;
            }
        }

        return true;
    }
}