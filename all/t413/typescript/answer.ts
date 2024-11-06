function getPalindromeList(n: number): number[] {
    const isPalindrome = (str: string): boolean => str === str.split('').reverse().join('');
    
    const palindromes = Array.from({ length: n }, (_, i) => i)
                             .filter(x => isPalindrome(x.toString()))
                             .map(Number);
    
    return palindromes;
}