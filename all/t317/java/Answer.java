/**
 * Count the number of letters in a string.
 *
 * @param str - The input string from which to count letters.
 * @return - The count of letters in the string.
 */
public class Answer {
    public static int countLetters(String str) {
        // Use a regular expression to match all letter characters (both uppercase and lowercase)
        String[] letters = str.split("[^a-zA-Z]");

        // Count the letters by filtering out empty strings
        int count = 0;
        for (String letter : letters) {
            count += letter.length();
        }

        // Return the count of letters
        return count;
    }

    public static void main(String[] args) {
        String input = "Hello, World!";
        int letterCount = countLetters(input);
        System.out.println("Number of letters: " + letterCount);
    }
}