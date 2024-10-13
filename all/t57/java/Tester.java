package org.real.temp;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import javax.imageio.ImageIO;
import javax.imageio.ImageWriteParam;
import javax.imageio.ImageWriter;
import javax.imageio.stream.ImageOutputStream;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.util.Iterator;

import static org.junit.jupiter.api.Assertions.assertThrows;
import static org.mockito.Mockito.*;

public class Tester {

    @Mock
    private ImageIO imageIO;

    @BeforeEach
    public void setUp() {
        MockitoAnnotations.openMocks(this);
    }

    @Test
    public void testSingleIconSize() throws IOException {
        // Mock the ImageIO.read method
        when(imageIO.read(any(FileImageInputStream.class))).thenReturn(new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB));

        convertPngToIco("source.png", "output.ico", new int[][]{{64, 64}});

        verify(imageIO).write(any(BufferedImage.class), any(String.class), any(File.class));
    }

    @Test
    public void testMultipleIconSizes() throws IOException {
        // Mock the ImageIO.read method
        when(imageIO.read(any(FileImageInputStream.class))).thenReturn(new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB));

        convertPngToIco("source.png", "output.ico", new int[][]{{16, 16}, {32, 32}, {64, 64}});

        verify(imageIO).write(any(BufferedImage.class), any(String.class), any(File.class));
    }

    @Test
    public void testDefaultIconSize() throws IOException {
        // Mock the ImageIO.read method
        when(imageIO.read(any(FileImageInputStream.class))).thenReturn(new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB));

        convertPngToIco("source.png", "output.ico");

        verify(imageIO).write(any(BufferedImage.class), any(String.class), any(File.class));
    }

    @Test
    public void testFileHandling() throws IOException {
        // Mock the ImageIO.read method
        when(imageIO.read(any(FileImageInputStream.class))).thenReturn(new BufferedImage(100, 100, BufferedImage.TYPE_INT_ARGB));

        convertPngToIco("source.png", "output.ico");

        verify(imageIO).write(any(BufferedImage.class), any(String.class), any(File.class));
    }

    @Test
    public void testInvalidImagePath() {
        assertThrows(FileNotFoundException.class, () -> {
            convertPngToIco("invalid.png", "output.ico");
        });
    }
}