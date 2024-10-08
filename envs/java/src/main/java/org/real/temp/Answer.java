package org.real.temp;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public List<String> readFileAndProcessLines(String path) {
        List<String> processedLines = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
        String line;
        while ((line = reader.readLine()) != null) {
        String processedLine = line.split("//")[0].trim(); // Remove inline comments
        if (!processedLine.isEmpty()) {
        processedLines.add(processedLine);
        }
        }
        } catch (IOException e) {
        throw new IllegalArgumentException("I/O error occurred while reading the file.", e);
        }
        return processedLines;
        }