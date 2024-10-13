package org.real.temp;

import javax.imageio.ImageIO;
import javax.imageio.ImageWriteParam;
import javax.imageio.ImageWriter;
import javax.imageio.stream.ImageOutputStream;
import java.awt.image.BufferedImage;
import java.io.*;
import java.util.Iterator;

public class Answer {

    /**
     * Convert a PNG image file to an ICO format file.
     *
     * @param pngFilePath  Path to the source PNG image file.
     * @param icoFilePath  Path to save the ICO file.
     * @param iconSizes    Array of dimensions specifying the sizes to include in the ICO file.
     */
    public static void convertPngToIco(String pngFilePath, String icoFilePath, int[][] iconSizes) {
        try (FileInputStream fis = new FileInputStream(pngFilePath);
             FileImageInputStream iiis = new FileImageInputStream(fis)) {
            BufferedImage bufferedImage = ImageIO.read(iiis);

            // Create a temporary file to store the ICO data
            File tempFile = File.createTempFile("temp", ".ico");
            tempFile.deleteOnExit();

            try (FileOutputStream fos = new FileOutputStream(tempFile);
                 ImageOutputStream ios = ImageIO.createImageOutputStream(fos)) {

                Iterator<ImageWriter> writers = ImageIO.getImageWritersByFormatName("ico");
                if (!writers.hasNext()) {
                    throw new IllegalStateException("No ICO writer found");
                }
                ImageWriter writer = writers.next();
                writer.setOutput(ios);

                // Set the parameters for the ICO format
                ImageWriteParam param = writer.getDefaultWriteParam();
                if (iconSizes != null && iconSizes.length > 0) {
                    param.setDestImageDimensions(iconSizes[0]);
                }

                // Write the image to the ICO file
                writer.write(null, ImageIO.getImageWriteParam(bufferedImage, writer, param), param);

                // Copy the temporary ICO file to the final destination
                try (FileInputStream fisTemp = new FileInputStream(tempFile);
                     FileOutputStream fosFinal = new FileOutputStream(icoFilePath)) {
                    byte[] buffer = new byte[1024];
                    int length;
                    while ((length = fisTemp.read(buffer)) > 0) {
                        fosFinal.write(buffer, 0, length);
                    }
                }

            } catch (IOException e) {
                System.err.println("Error writing ICO file: " + e.getMessage());
            }

        } catch (IOException e) {
            System.err.println("Error reading PNG file: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        String pngFilePath = "path/to/source.png";
        String icoFilePath = "path/to/output.ico";
        int[][] iconSizes = {{32, 32}};

        convertPngToIco(pngFilePath, icoFilePath, iconSizes);
    }
}