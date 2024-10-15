package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertTrue;

public class Tester {

    @Test
    public void testFormatBytes_zeroBytes() {
        String result = ByteFormatter.formatBytes(0, new ByteFormatter.FormatOptions(null, "normal"));
        assertTrue(result.equals("0 Byte") || result.equals("0 B"));
    }

    @Test
    public void testFormatBytes_2048Bytes() {
        String result = ByteFormatter.formatBytes(2048, new ByteFormatter.FormatOptions(null, "normal"));
        assertTrue(result.equals("2 KB") || result.equals("2.0 KB"));
    }

    @Test
    public void testFormatBytes_accurate_2048Bytes() {
        String result = ByteFormatter.formatBytes(2048, new ByteFormatter.FormatOptions(null, "accurate"));
        assertTrue(result.equals("2 KiB") || result.equals("2.0 KiB"));
    }

    @Test
    public void testFormatBytes_5242880Bytes() {
        String result = ByteFormatter.formatBytes(5242880, new ByteFormatter.FormatOptions(null, "normal"));
        assertTrue(result.equals("5 MB") || result.equals("5.0 MB"));
    }

    @Test
    public void testFormatBytes_accurate_5242880Bytes() {
        String result = ByteFormatter.formatBytes(5242880, new ByteFormatter.FormatOptions(2, "accurate"));
        assertTrue(result.equals("5.00 MiB"));
    }
}