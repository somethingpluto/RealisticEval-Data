package org.real.temp;


public class Answer {

    public static long powerTail(long x, long y) {
        return powerTail(x, y, 1);
    }

    private static long powerTail(long x, long y, long acc) {
        // Base case: if exponent y is 0, return the accumulated result
        if (y == 0) {
            return acc;  // Return accumulated result
        }

        // Tail-recursive call with decremented exponent and updated accumulator
        return powerTail(x, y - 1, acc * x);
    }
}