import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Answer {

    /**
     * Converts an image to a binary representation. Convert the image to black and white mode,
     * that is, each pixel is represented by only 1 bit, with a white pixel value of 255 and a black
     * pixel value of 0.
     *
     * @param imagePath The file path of the image to convert.
     * @return A list of bits representing the image, where 1 is for white pixels and 0 is for black pixels.
     */
    public static List<Integer> convertImageToBits(String imagePath) {
        try {
            BufferedImage image = ImageIO.read(new File(imagePath));
            int width = image.getWidth();
            int height = image.getHeight();

            List<Integer> bits = new ArrayList<>();
            for (int y = 0; y < height; y++) {
                for (int x = 0; x < width; x++) {
                    // Get RGB value of the pixel
                    int rgb = image.getRGB(x, y);
                    // Extract red component (since it's in grayscale)
                    int r = (rgb >> 16) & 0xFF;
                    // Convert to black and white based on the average of RGB values
                    if (r > 127) {
                        bits.add(1); // White
                    } else {
                        bits.add(0); // Black
                    }
                }
            }

            return bits;
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }

}