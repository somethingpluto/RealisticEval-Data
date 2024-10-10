package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testConvertFileSize() {
        // Assuming the convertFileSize method is implemented in a class named FileSizeConverter
        FileSizeConverter converter = new FileSizeConverter();

        // Test cases
        assertEquals("2KB", converter.convertFileSize(2120));
        assertEquals("1MB", converter.convertFileSize(1048576)); // 1MB = 1024 * 1024 bytes
        assertEquals("5GB", converter.convertFileSize(5368709120L)); // 5GB = 5 * 1024 * 1024 * 1024 bytes
        assertEquals("1TB", converter.convertFileSize(1099511627776L)); // 1TB = 1024 * 1024 * 1024 * 1024 * 1024 bytes
    }
}

// Example implementation of the FileSizeConverter class
class FileSizeConverter {
    public String convertFileSize(long sizeBytes) {
        if (sizeBytes < 1024) return sizeBytes + "B";
        else if (sizeBytes < 1024 * 1024) return Math.round((double) sizeBytes / 1024) + "KB";
        else if (sizeBytes < 1024 * 1024 * 1024) return Math.round((double) sizeBytes / (1024 * 1024)) + "MB";
        else if (sizeBytes < 1024 * 1024 * 1024 * 1024) return Math.round((double) sizeBytes / (1024 * 1024 * 1024)) + "GB";
        else return Math.round((double) sizeBytes / (1024 * 1024 * 1024 * 1024)) + "TB";
    }
}