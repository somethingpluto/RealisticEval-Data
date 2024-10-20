package org.real.temp;

import org.junit.Test;

import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void shouldReturnFilenameUnchangedIfUnderMaxLength() {
        assertEquals("file.txt", compressFilename("file.txt", 10));
    }

    @Test
    public void shouldTruncateAndAppendIfFilenameExceedsMaxLength() {
        assertEquals("verylongfi***.txt", compressFilename("verylongfilename.txt", 10));
    }

    @Test
    public void shouldPreserveFileExtensionAfterCompression() {
        assertEquals("docum***.pdf", compressFilename("document.pdf", 5));
    }

    @Test
    public void shouldTruncateAndAppendIfFilenameExceeds() {
        assertEquals("sh***.mp3", compressFilename("short.mp3", 2));
    }
}