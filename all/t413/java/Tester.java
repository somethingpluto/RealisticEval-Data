import java.util.ArrayList;
import java.util.List;

public class NumberUtils {

    public static List<Integer> getPalindromeList(int n) {
        List<Integer> palindromes = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            if (isPalindrome(i)) {
                palindromes.add(i);
            }
        }
        return palindromes;
    }

    private static boolean isPalindrome(int number) {
        String str = Integer.toString(number);
        int left = 0;
        int right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}