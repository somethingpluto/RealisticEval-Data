/**
 * Increments the entered number.
 * If the number is non-positive (<= 0), returns the original value.
 * If the number is positive, returns the value plus 1.
 *
 * @param num The number to increment.
 * @return The incremented value or the original number.
 */
public class Answer {
    public static int incrementNumber(int num) {
        if (num > 0) {
            return num + 1; // Increment if positive
        }
        return num; // Return original value if non-positive
    }

    public static void main(String[] args) {
        // Example usage
        System.out.println(incrementNumber(5));  // Outputs 6
        System.out.println(incrementNumber(0));  // Outputs 0
        System.out.println(incrementNumber(-3)); // Outputs -3
    }
}