/**
 * Finds and returns the smallest letter in a sorted array that is larger than the given target letter.
 * If the target letter is greater than or equal to all letters in the array, the function returns the first letter in the array.
 *
 * @param letters - A sorted array of letters.
 * @param target - The target letter to find the next greatest letter for.
 * @returns The smallest letter in the array that is larger than the target letter.
 */
public class LetterFinder {
    public static char nextGreatestLetter(char[] letters, char target) {
        int low = 0;
        int high = letters.length;

        // Perform binary search to find the smallest letter greater than the target
        while (low < high) {
            int mid = low + (high - low) / 2;

            // If the mid letter is less than or equal to the target, move to the right half
            if (letters[mid] <= target) {
                low = mid + 1;
            } else {
                // Otherwise, move to the left half
                high = mid;
            }
        }

        // Return the letter at the calculated position, wrapping around if necessary
        return letters[low % letters.length];
    }

    public static void main(String[] args) {
        char[] letters = {'c', 'f', 'j'};
        char target = 'a';
        System.out.println(nextGreatestLetter(letters, target)); // Output: c
    }
}