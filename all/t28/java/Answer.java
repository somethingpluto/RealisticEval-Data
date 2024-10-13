package org.real.temp;

public class Answer {

    /**
     * Prints the status of each bit (0 or 1) in the given section of memory.
     *
     * @param memorySection A byte array representing the section of memory to be read.
     */
    public static void printMemoryBits(byte[] memorySection) {
        for (byte b : memorySection) {
            for (int i = 7; i >= 0; i--) {
                int bit = (b >> i) & 1;
                System.out.print(bit);
            }
            System.out.println(); // Move to the next line after printing all bits of a byte
        }
    }

    public static void main(String[] args) {
        // Example usage
        byte[] memorySection = new byte[]{(byte) 0xAA, (byte) 0x55};
        printMemoryBits(memorySection);
    }
}