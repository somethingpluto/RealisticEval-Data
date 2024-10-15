import java.nio.ByteBuffer;

public class HashCompressor {

    /**
     * The input hash buffer is compressed into a number letter string of length no less than 5
     *
     * @param hash - The hash buffer to be compressed.
     * @return A compressed string representation of the hash.
     */
    public static String compressHash(ByteBuffer hash) {
        // Convert the hash buffer to a number in base 16 (hexadecimal)
        String hexString = bytesToHex(hash);
        long num = Long.parseLong(hexString, 16);

        // Define the base and alphabet for encoding
        final int base = 62;
        final String alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";

        // Initialize the result string
        StringBuilder result = new StringBuilder();

        // Convert the number to the desired base (base 62) and construct the compressed string
        while (result.length() < 5) {
            int remainder = (int) (num % base);
            result.append(alphabet.charAt(remainder));
            num /= base;
        }

        return result.toString();
    }

    // Helper method to convert byte array to hex string
    private static String bytesToHex(ByteBuffer buffer) {
        StringBuilder hexString = new StringBuilder();
        while (buffer.hasRemaining()) {
            String hex = Integer.toHexString(buffer.get() & 0xFF);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex);
        }
        return hexString.toString();
    }

    public static void main(String[] args) {
        // Example usage
        ByteBuffer hashBuffer = ByteBuffer.wrap(new byte[]{0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC, 0xDE, 0xF0});
        String compressed = compressHash(hashBuffer);
        System.out.println(compressed); // Output the compressed string
    }
}