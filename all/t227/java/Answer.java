package org.real.temp;

import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.HashSet;
import java.util.Set;
import javax.imageio.ImageIO;

public class Answer {

    /**
     * Count the number of unique colors in an image.
     *
     * @param imagePath Path to the image file.
     * @return The number of unique colors in the image.
     */
    public static int countUniqueColors(String imagePath) {
        try {
            // Read the image file
            BufferedImage image = ImageIO.read(new File(imagePath));

            if (image == null) {
                throw new IOException("Image could not be read.");
            }

            // Get the width and height of the image
            int width = image.getWidth();
            int height = image.getHeight();

            // Use a set to store unique RGB values
            Set<Integer> uniqueColors = new HashSet<>();

            // Iterate over each pixel in the image
            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    // Get the RGB value of the pixel
                    int rgb = image.getRGB(x, y);
                    // Add the RGB value to the set
                    uniqueColors.add(rgb);
                }
            }

            // Return the number of unique colors
            return uniqueColors.size();
        } catch (IOException e) {
            e.printStackTrace();
            return -1; // Return -1 on error
        }
    }

    public static void main(String[] args) {
        String imagePath = "path/to/your/image.jpg";
        int uniqueColorCount = countUniqueColors(imagePath);
        System.out.println("Number of unique colors: " + uniqueColorCount);
    }
}