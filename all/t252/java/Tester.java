package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.json.JSONObject;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

public class Tester {

    private BitSequenceEncoder bitSequenceEncoder;

    @BeforeEach
    public void setUp() {
        bitSequenceEncoder = new BitSequenceEncoder();
    }

    @Test
    public void testEncodeIntegerBits() {
        JSONObject jsonObject = new JSONObject();
        jsonObject.put("bits", 255);

        String encodedJson = bitSequenceEncoder.encode(jsonObject.toString());

        // Assuming the expected output is {"bits": "11111111"}
        assertEquals("{\"bits\": \"11111111\"}", encodedJson);
    }
}