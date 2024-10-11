package org.real.temp;

public class Answer {

    /**
     * Prints the status of each bit (0 or 1) in the given section of memory.
     * For example:
     *     input: 0b10101010
     *     output: 10101010
     * If have multiple bytes use \n split
     * For example:
     *     input: [0b11001100, 0b11110000]
     *     output: 11001100\n11110000
     *
     * @param memorySection A byte array representing the section of memory to be read.
     */
    public static void printMemoryBits(byte[] memorySection) {
        StringBuilder result = new StringBuilder();

        for (byte b : memorySection) {
            String binaryString = String.format("%8s", Integer.toBinaryString(b & 0xFF)).replace(' ', '0');
            if (result.length() > 0) {
                result.append("\n");
            }
            result.append(binaryString);
        }

        System.out.println(result.toString());
    }

    public static void main(String[] args) {
        // Example usage
        byte[] memorySection = { (byte) 0b11001100, (byte) 0b11110000 };
        printMemoryBits(memorySection);
    }
}