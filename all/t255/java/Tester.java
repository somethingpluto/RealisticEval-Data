package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.*;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;
import java.util.List;

public class TesterTest extends TestCase {

    private Tester tester;

    @Override
    protected void setUp() throws Exception {
        super.setUp();
        tester = new Tester();
    }

    @Test
    public void testConvertImageToBits() throws Exception {
        String imagePath = "path/to/your/test/image.png";
        List<Integer> bits = tester.convertImageToBits(imagePath);

        // Add assertions based on expected output
        assertEquals(8 * 8, bits.size()); // Assuming a 8x8 image
        assertTrue(bits.contains(0)); // Check for black pixels
        assertTrue(bits.contains(1)); // Check for white pixels
    }

    @Test(expected = Exception.class)
    public void testConvertImageToBitsWithInvalidPath() throws Exception {
        String invalidImagePath = "path/to/nonexistent/image.png";
        tester.convertImageToBits(invalidImagePath);
    }
}