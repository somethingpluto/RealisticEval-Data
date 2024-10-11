function getPalindromeList(n: number): number[] {
    /**
     * Filter out the number of palindrome within any number n. Palindrome numbers are numbers with the same correction and reverse readings, such as 121, 1331
     *
     * @param {number} n - range number
     * @returns {number[]} Palindrome numbers
     */
    
    const isPalindrome = (num: number): boolean => {
        const strNum = num.toString();
        return strNum === strNum.split('').reverse().join('');
    };

    const palindromeList: number[] = [];
    for (let i = 0; i <= n; i++) {
        if (isPalindrome(i)) {
            palindromeList.push(i);
        }
    }

    return palindromeList;
}