package org.real.temp;

import static org.junit.jupiter.api.Assertions.assertEquals;
import org.junit.jupiter.api.Test;

public class Tester {

    @Test
    public void testConvertImageToBits() {
        // Assuming convertImageToBits is implemented in ImageConverter class
        ImageConverter converter = new ImageConverter();

        // Example image path (replace with actual image path)
        String imagePath = "path/to/your/image.jpg";

        // Call the method to be tested
        List<Integer> result = converter.convertImageToBits(imagePath);

        // Expected result (replace with actual expected result)
        List<Integer> expectedResult = Arrays.asList(0, 1, 0, 1, 1, 0, 0, 1);

        // Assert the result
        assertEquals(expectedResult, result);
    }
}
