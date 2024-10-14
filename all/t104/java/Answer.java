import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.ByteArrayInputStream;
import java.io.IOException;

public class ThreadConverter {

    /**
     * Converts a thread object to a byte array representing the JSON file.
     *
     * @param thread - The thread object to be converted.
     * @returns ByteArrayInputStream - A stream representing the JSON file.
     * @throws IOException - If there's an error during conversion.
     */
    public ByteArrayInputStream convertThreadToJSONFile(Object thread) throws IOException {
        ObjectMapper objectMapper = new ObjectMapper();
        String jsonString = objectMapper.writeValueAsString(thread);  // Convert the thread object to a JSON string
        return new ByteArrayInputStream(jsonString.getBytes());  // Encode the JSON string as a byte array stream
    }
}