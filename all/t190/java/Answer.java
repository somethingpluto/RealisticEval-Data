package org.real.temp;

import java.nio.ByteBuffer;

public class Answer {

    public static float hexStringToFloat(String hexStr) {
        int intValue = Integer.parseUnsignedInt(hexStr, 16);
        return ByteBuffer.allocate(4).putInt(intValue).getFloat(0);
    }
}