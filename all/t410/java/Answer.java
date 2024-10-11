package org.real.temp;

import java.util.Arrays;

public class Answer {

    public static boolean checkXorSum(int[][] combination) {
        int xor1 = combination[0][0] ^ combination[0][1];
        int xor2 = combination[1][0] ^ combination[1][1];

        return xor1 == 3 && xor2 == 6;
    }
}