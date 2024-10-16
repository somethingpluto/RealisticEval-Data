/**
 * Converts the array of Boolean values to a binary string representation,
 * which converts to the character '1' if the Boolean value is true.
 * Otherwise, it is converted to the character '0', and the final string is returned.
 *
 * @param boolArray An array of boolean values.
 * @return A binary string where '1' represents true and '0' represents false.
 */
public class BooleanArrayToBinaryString {

    public static String boolArrayToBinaryString(boolean[] boolArray) {
        StringBuilder binaryString = new StringBuilder();
        for (boolean value : boolArray) {
            binaryString.append(value ? "1" : "0");
        }
        return binaryString.toString();
    }

    public static void main(String[] args) {
        boolean[] boolArray = {true, false, true, true, false};
        String result = boolArrayToBinaryString(boolArray);
        System.out.println(result); // Output: 10110
    }
}