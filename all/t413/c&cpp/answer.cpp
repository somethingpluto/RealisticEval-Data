#include <iostream>
#include <vector>

bool isPalindrome(int num) {
    int originalNum = num;
    int reversedNum = 0;

    while(num != 0) {
        int digit = num % 10;
        reversedNum = reversedNum * 10 + digit;
        num /= 10;
    }

    return originalNum == reversedNum;
}

std::vector<int> getPalindromeList(int n) {
    std::vector<int> palindromes;

    for(int i=1; i<=n; i++) {
        if(isPalindrome(i)) {
            palindromes.push_back(i);
        }
    }

    return palindromes;
}