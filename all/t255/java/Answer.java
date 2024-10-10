import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Answer {
    public static List<Integer> convertImageToBits(String imagePath) throws Exception {
        // Load the image from the given path
        BufferedImage image = ImageIO.read(new File(imagePath));

        int width = image.getWidth();
        int height = image.getHeight();

        List<Integer> bits = new ArrayList<>();

        for(int y=0; y<height; y++) {
            for(int x=0; x<width; x++) {
                // Get the color of the current pixel
                int rgb = image.getRGB(x, y);

                // Extract the red component
                int r = (rgb >> 16) & 0xFF;

                // Check if the pixel is white
                if(r == 255)
                    bits.add(1);
                else
                    bits.add(0);
            }
        }

        return bits;
    }
}