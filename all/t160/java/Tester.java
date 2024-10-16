package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void shouldReturnFilenameUnchangedIfUnderMaxLength() {
        assertEquals("file.txt", compressFileName("file.txt", 10));
    }

    @Test
    public void shouldTruncateAndAppendIfFilenameExceedsMaxLength() {
        assertEquals("verylongfi***.txt", compressFileName("verylongfilename.txt", 10));
    }

    @Test
    public void shouldPreserveFileExtensionAfterCompression() {
        assertEquals("docum***.pdf", compressFileName("document.pdf", 5));
    }

    @Test
    public void shouldTruncateAndAppendIfFilenameExceeds() {
        assertEquals("sh***.mp3", compressFileName("short.mp3", 2));
    }
}