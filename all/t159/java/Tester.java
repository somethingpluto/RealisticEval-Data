package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class Tester {

    @Test
    public void testRemoveFileExtensionStandardFile() {
        assertEquals("document", FileUtils.removeFileExtension("document.txt"));
    }

    @Test
    public void testRemoveFileExtensionNoExtension() {
        assertEquals("document", FileUtils.removeFileExtension("document"));
    }

    @Test
    public void testRemoveFileExtensionMultipleDots() {
        assertEquals("my.file.with.many.extensions", FileUtils.removeFileExtension("my.file.with.many.extensions.pdf"));
    }

    @Test
    public void testRemoveFileExtensionEndsWithDot() {
        assertEquals("document", FileUtils.removeFileExtension("document."));
    }

    @Test
    public void testRemoveFileExtensionWithDotsInPath() {
        assertEquals("path.to/my.file", FileUtils.removeFileExtension("path.to/my.file.txt"));
    }
}