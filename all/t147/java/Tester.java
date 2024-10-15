import static org.junit.Assert.assertEquals;
import org.junit.Test;
import java.nio.ByteBuffer;
import java.nio.charset.StandardCharsets;

public class Tester {

    public static String arrayBufferToString(ByteBuffer buffer) {
        byte[] byteArray = new byte[buffer.remaining()];
        buffer.get(byteArray);
        return new String(byteArray, StandardCharsets.UTF_8);
    }

    @Test
    public void testEmptyBuffer() {
        ByteBuffer buffer1 = ByteBuffer.allocate(0);
        String result = arrayBufferToString(buffer1);
        assertEquals("", result); // Expected: ""
    }

    @Test
    public void testSingleCharacter() {
        ByteBuffer buffer2 = ByteBuffer.wrap("A".getBytes(StandardCharsets.UTF_8));
        String result = arrayBufferToString(buffer2);
        assertEquals("A", result); // Expected: "A"
    }

    @Test
    public void testHelloString() {
        ByteBuffer buffer3 = ByteBuffer.wrap("Hello".getBytes(StandardCharsets.UTF_8));
        String result = arrayBufferToString(buffer3);
        assertEquals("Hello", result); // Expected: "Hello"
    }

    @Test
    public void testMultipleCharacters() {
        ByteBuffer buffer4 = ByteBuffer.wrap("Hello, World!".getBytes(StandardCharsets.UTF_8));
        String result = arrayBufferToString(buffer4);
        assertEquals("Hello, World!", result); // Expected: "Hello, World!"
    }

    @Test
    public void testInputBufferUnchanged() {
        String input = "Test input";
        ByteBuffer buffer8 = ByteBuffer.wrap(input.getBytes(StandardCharsets.UTF_8));
        arrayBufferToString(buffer8);
        String result = new String(buffer8.array(), buffer8.position(), buffer8.remaining(), StandardCharsets.UTF_8);
        assertEquals(input, result); // Check if the buffer content remains unchanged
    }
}