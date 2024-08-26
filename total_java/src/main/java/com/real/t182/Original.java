package com.real.t182;

import java.io.BufferedInputStream;
import java.io.BufferedOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.nio.file.FileAlreadyExistsException;
import java.util.Arrays;

public class Original {
    static int BUFFER_SIZE = 1024;

    public static void main(String[] args) throws IOException {
        System.out.println(Arrays.toString(args));
        if (args.length != 2) { //block written by copilot
            System.out.println("Usage: java FileCopy <source file> <target file>");
            throw new IllegalArgumentException("Invalid number of arguments");
        }

        String input = args[0];
        String destination = args[1];

        File inputFile = new File(input);
        File outputFile = new File(destination);

        if (!inputFile.exists()) {
            System.out.println("File " + input + " does not exist");
            throw new FileNotFoundException("File does not exist");
        }

        if (outputFile.exists()) {
            System.out.println("File " + destination + " already exists");
            throw new FileAlreadyExistsException("File already exists");
        }

        long startTime = 0;

        try (InputStream inputStream = new BufferedInputStream(new FileInputStream(inputFile)); OutputStream outputStream = new BufferedOutputStream(new FileOutputStream(outputFile))) {
            byte[] buffer = new byte[BUFFER_SIZE];
            int length;
            startTime = System.currentTimeMillis();

            while ((length = inputStream.read(buffer)) > 0) {
                outputStream.write(buffer, 0, length);
            }
        }

        System.out.println("Time taken: " + (System.currentTimeMillis() - startTime) + "ms");

    }
}
