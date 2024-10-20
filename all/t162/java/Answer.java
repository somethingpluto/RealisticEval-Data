package org.real.temp;
public class Answer {

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