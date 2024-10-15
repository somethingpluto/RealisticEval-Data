package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testBytesToSize_KB() {
        assertEquals("1.00 KB", ByteConverter.bytesToSize(1024));
        assertEquals("2.00 KB", ByteConverter.bytesToSize(2048));
    }

    @Test
    public void testBytesToSize_MB() {
        assertEquals("1.00 MB", ByteConverter.bytesToSize(1048576));
        assertEquals("2.00 MB", ByteConverter.bytesToSize(2097152));
    }

    @Test
    public void testBytesToSize_GB() {
        assertEquals("1.00 GB", ByteConverter.bytesToSize(1073741824));
        assertEquals("2.00 GB", ByteConverter.bytesToSize(2147483648L));
    }

    @Test
    public void testBytesToSize_TB() {
        assertEquals("1.00 TB", ByteConverter.bytesToSize(1099511627776L));
        assertEquals("2.00 TB", ByteConverter.bytesToSize(2199023255552L));
    }
}