package org.real.temp;

import java.util.ArrayList;
import java.util.List;

public class Answer {

    public List<Integer> getPalindromeList(int n) {
        List<Integer> palindromeList = new ArrayList<>();

        for (int num = 1; num <= n; num++) {
            if (isPalindrome(num)) {
                palindromeList.add(num);
            }
        }

        return palindromeList;
    }
    
}