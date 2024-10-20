package org.real.temp;

import org.junit.Test;
import org.junit.Rule;
import org.junit.rules.ExpectedException;
import org.mockito.Mockito;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;

import static org.mockito.Mockito.*;

public class Tester {

    @Rule
    public ExpectedException thrown = ExpectedException.none();

    @Test
    public void testSingleIconSize() throws Exception {
        BufferedImage mockImage = mock(BufferedImage.class);
        when(ImageIO.read(new File("source.png"))).thenReturn(mockImage);

        ConvertPngToIco.convertPngToIco("source.png", "output.ico", new int[][]{{64, 64}});

        verify(mockImage).save("output.ico", "ICO", new int[][]{{64, 64}});
    }

    @Test
    public void testMultipleIconSizes() throws Exception {
        BufferedImage mockImage = mock(BufferedImage.class);
        when(ImageIO.read(new File("source.png"))).thenReturn(mockImage);

        ConvertPngToIco.convertPngToIco("source.png", "output.ico", new int[][]{{16, 16}, {32, 32}, {64, 64}});

        verify(mockImage).save("output.ico", "ICO", new int[][]{{16, 16}, {32, 32}, {64, 64}});
    }

    @Test
    public void testDefaultIconSize() throws Exception {
        BufferedImage mockImage = mock(BufferedImage.class);
        when(ImageIO.read(new File("source.png"))).thenReturn(mockImage);

        ConvertPngToIco.convertPngToIco("source.png", "output.ico");

        verify(mockImage).save("output.ico", "ICO", new int[][]{{32, 32}});
    }

    @Test
    public void testFileHandling() throws Exception {
        BufferedImage mockImage = mock(BufferedImage.class);
        when(ImageIO.read(new File("source.png"))).thenReturn(mockImage);

        ConvertPngToIco.convertPngToIco("source.png", "output.ico");

        verify(mockImage, times(1)).save("output.ico", "ICO", new int[][]{{32, 32}});
    }

    @Test
    public void testInvalidImagePath() throws Exception {
        thrown.expect(FileNotFoundException.class);
        ConvertPngToIco.convertPngToIco("invalid.png", "output.ico");
    }
}
