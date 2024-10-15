import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

public class ArrayBufferConverter {
    public static String arrayBufferToString(ByteBuffer buffer) {
        // Create a byte array from the ByteBuffer
        byte[] byteArray = new byte[buffer.remaining()];
        buffer.get(byteArray);

        // Convert the byte array to a string using UTF-8 encoding
        return new String(byteArray, StandardCharsets.UTF_8);
    }
}