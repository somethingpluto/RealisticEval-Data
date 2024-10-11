function getPalindromeList(n) {
    // Helper function to check if a number is a palindrome
    function isPalindrome(num) {
        let str = num.toString();
        return str === str.split('').reverse().join('');
    }

    // Initialize an array to store palindrome numbers
    let palindromeList = [];

    // Loop through all numbers in the given range
    for(let i = 0; i <= n; i++) {
        if(isPalindrome(i)) {
            palindromeList.push(i);
        }
    }

    return palindromeList;
}