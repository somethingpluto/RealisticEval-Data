package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
public class Tester {

    @Test
    public void testRemoveFileExtensionStandardFile() {
        assertEquals("document", removeFileExtension("document.txt"));
    }

    @Test
    public void testRemoveFileExtensionNoExtension() {
        assertEquals("document", removeFileExtension("document"));
    }

    @Test
    public void testRemoveFileExtensionMultipleDots() {
        assertEquals("my.file.with.many.extensions", removeFileExtension("my.file.with.many.extensions.pdf"));
    }

    @Test
    public void testRemoveFileExtensionEndsWithDot() {
        assertEquals("document", removeFileExtension("document."));
    }

    @Test
    public void testRemoveFileExtensionWithDotsInPath() {
        assertEquals("path.to/my.file", removeFileExtension("path.to/my.file.txt"));
    }
}