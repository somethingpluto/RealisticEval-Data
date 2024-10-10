package org.real.temp;

import com.fasterxml.jackson.core.JsonGenerator;
import com.fasterxml.jackson.databind.SerializerProvider;
import com.fasterxml.jackson.databind.ser.std.StdSerializer;

import java.io.IOException;

public class BitSequenceEncoder extends StdSerializer<Object> {

    public BitSequenceEncoder() {
        this(null);
    }

    public BitSequenceEncoder(Class<Object> t) {
        super(t);
    }

    @Override
    public void serialize(Object value, JsonGenerator gen, SerializerProvider provider) throws IOException {
        // Your logic here
    }
}