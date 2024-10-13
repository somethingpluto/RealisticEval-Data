package org.real.temp;

import java.io.File;
import java.util.ArrayList;
import java.util.List;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.NodeList;
import org.w3c.dom.Element;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;
import java.io.FileWriter;
import java.io.IOException;

public class Answer {

    /**
     * Convert an XML file into a CSV file. Each <sequence> tag is treated as a row,
     * and each sub-element within <sequence> is treated as a column.
     *
     * @param xmlFile Path to the XML file.
     * @throws Exception if any error occurs during XML parsing or CSV writing.
     */
    public static void xmlToCSV(String xmlFile) throws Exception {
        // Parse the XML file
        File inputFile = new File(xmlFile);
        DocumentBuilderFactory dbFactory = DocumentBuilderFactory.newInstance();
        DocumentBuilder dBuilder = dbFactory.newDocumentBuilder();
        Document doc = dBuilder.parse(inputFile);
        doc.getDocumentElement().normalize();

        // Prepare a list to hold all rows
        List<String[]> rows = new ArrayList<>();

        // Get the root element
        Element rootElement = doc.getDocumentElement();

        // Iterate over each <sequence> element in the XML file
        NodeList sequenceList = rootElement.getElementsByTagName("sequence");
        for (int i = 0; i < sequenceList.getLength(); i++) {
            Element sequence = (Element) sequenceList.item(i);
            String[] row = new String[sequence.getChildNodes().getLength()];

            // Iterate over each child of the <sequence> element
            int j = 0;
            for (int k = 0; k < sequence.getChildNodes().getLength(); k++) {
                if (sequence.getChildNodes().item(k) instanceof Element) {
                    Element child = (Element) sequence.getChildNodes().item(k);
                    row[j++] = child.getTextContent();
                }
            }

            rows.add(row);
        }

        // Write the list of rows to a CSV file
        try (CSVPrinter printer = new CSVPrinter(new FileWriter(xmlFile + ".csv"), CSVFormat.DEFAULT)) {
            // Write header
            String[] header = {"tag1", "tag2", "tag3"}; // Adjust the header based on the actual tags
            printer.printRecord(header);

            // Write data
            for (String[] row : rows) {
                printer.printRecord(row);
            }
        } catch (IOException e) {
            throw new IOException("Error writing CSV file", e);
        }
    }

    public static void main(String[] args) {
        try {
            xmlToCSV("path/to/your/xmlfile.xml");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}