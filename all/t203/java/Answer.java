package org.real.temp;

import java.util.List;
import java.util.ArrayList;
import java.util.Collections;

public class Answer {
    
    public static void reverseRange(List<Integer> v, int a, int b) {
        if (a < 0 || b >= v.size() || a > b) {
            System.err.println("Invalid indices");
            return;
        }
        Collections.reverse(v.subList(a, b + 1));
    }

    public static void main(String[] args) {
        // Example usage
        List<Integer> numbers = new ArrayList<>();
        Collections.addAll(numbers, 1, 2, 3, 4, 5);
        reverseRange(numbers, 1, 3);
        System.out.println(numbers);  // Output will be [1, 4, 3, 2, 5]
    }
}