import java.util.Arrays;

public class Answer {

    /**
     * Produces a character array of length 52 containing all lowercase and uppercase letters in alphabetical order.
     *
     * @return An array of alphabet characters from 'a' to 'z' and 'A' to 'Z'.
     */
    public static char[] getAllAlphabets() {
        final int alphabetCount = 26; // Number of letters in the English alphabet
        char[] alphabets = new char[alphabetCount * 2];

        for (int index = 0; index < alphabets.length; index++) {
            // Determine the character based on the index:
            if (index < alphabetCount) {
                // Lowercase letters
                alphabets[index] = (char) (97 + index); // 'a' starts at char code 97
            } else {
                // Uppercase letters
                alphabets[index] = (char) (65 + index - alphabetCount); // 'A' starts at char code 65
            }
        }

        return alphabets;
    }

    public static void main(String[] args) {
        char[] alphabetArray = getAllAlphabets();
        System.out.println(Arrays.toString(alphabetArray));
    }
}