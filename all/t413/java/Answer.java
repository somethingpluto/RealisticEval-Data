package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    public static List<Integer> getPalindromeList(int n) {
        List<Integer> palindromeList = new ArrayList<>();

        for(int i=0; i<=n; i++){
            if(isPalindrome(i)){
                palindromeList.add(i);
            }
        }

        return palindromeList;
    }

    private static boolean isPalindrome(int num){
        int originalNum = num, reversedNum = 0, remainder;

        while(num != 0){
            remainder = num % 10;
            reversedNum = reversedNum * 10 + remainder;
            num /= 10;
        }

        return originalNum == reversedNum;
    }
}