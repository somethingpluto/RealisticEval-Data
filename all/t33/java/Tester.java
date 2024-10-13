package org.real.temp;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import java.io.ByteArrayInputStream;
import java.io.InputStream;
import java.util.List;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVPrinter;
import org.apache.commons.csv.CSVRecord;

class Tester {

    /**
     * Tests converting a single sequence in the XML to a DataFrame.
     */
    @Test
    void testSingleSequence() throws Exception {
        String xmlData = "<root>\n" +
                         "  <sequence>\n" +
                         "    <name>John</name>\n" +
                         "    <age>30</age>\n" +
                         "  </sequence>\n" +
                         "</root>";

        InputStream xmlInput = new ByteArrayInputStream(xmlData.getBytes());
        List<String[]> rows = xmlToCSV(xmlInput);

        List<String[]> expected = List.of(new String[]{"name", "age"}, new String[]{"John", "30"});
        assertEquals(expected.size(), rows.size());

        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i).length, rows.get(i).length);
            for (int j = 0; j < expected.get(i).length; j++) {
                assertEquals(expected.get(i)[j], rows.get(i)[j]);
            }
        }
    }

    /**
     * Tests converting multiple sequences in the XML to a DataFrame.
     */
    @Test
    void testMultipleSequences() throws Exception {
        String xmlData = "<root>\n" +
                         "  <sequence>\n" +
                         "    <name>Alice</name>\n" +
                         "    <age>25</age>\n" +
                         "  </sequence>\n" +
                         "  <sequence>\n" +
                         "    <name>Bob</name>\n" +
                         "    <age>22</age>\n" +
                         "  </sequence>\n" +
                         "</root>";

        InputStream xmlInput = new ByteArrayInputStream(xmlData.getBytes());
        List<String[]> rows = xmlToCSV(xmlInput);

        List<String[]> expected = List.of(
            new String[]{"name", "age"},
            new String[]{"Alice", "25"},
            new String[]{"Bob", "22"}
        );
        assertEquals(expected.size(), rows.size());

        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i).length, rows.get(i).length);
            for (int j = 0; j < expected.get(i).length; j++) {
                assertEquals(expected.get(i)[j], rows.get(i)[j]);
            }
        }
    }

    /**
     * Tests converting an empty sequence in the XML to a DataFrame.
     */
    @Test
    void testEmptySequence() throws Exception {
        String xmlData = "<root>\n" +
                         "  <sequence/>\n" +
                         "</root>";

        InputStream xmlInput = new ByteArrayInputStream(xmlData.getBytes());
        List<String[]> rows = xmlToCSV(xmlInput);

        List<String[]> expected = List.of(new String[]{"name", "age"}, new String[]{null, null});
        assertEquals(expected.size(), rows.size());

        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i).length, rows.get(i).length);
            for (int j = 0; j < expected.get(i).length; j++) {
                assertEquals(expected.get(i)[j], rows.get(i)[j]);
            }
        }
    }

    /**
     * Tests converting mixed content in the XML to a DataFrame.
     */
    @Test
    void testMixedContent() throws Exception {
        String xmlData = "<root>\n" +
                         "  <sequence>\n" +
                         "    <name>Chris</name>\n" +
                         "  </sequence>\n" +
                         "  <sequence>\n" +
                         "    <age>28</age>\n" +
                         "  </sequence>\n" +
                         "</root>";

        InputStream xmlInput = new ByteArrayInputStream(xmlData.getBytes());
        List<String[]> rows = xmlToCSV(xmlInput);

        List<String[]> expected = List.of(
            new String[]{"name", "age"},
            new String[]{"Chris", null},
            new String[]{null, "28"}
        );
        assertEquals(expected.size(), rows.size());

        for (int i = 0; i < expected.size(); i++) {
            assertEquals(expected.get(i).length, rows.get(i).length);
            for (int j = 0; j < expected.get(i).length; j++) {
                assertEquals(expected.get(i)[j], rows.get(i)[j]);
            }
        }
    }

    /**
     * Tests converting no sequences in the XML to a DataFrame.
     */
    @Test
    void testNoSequences() throws Exception {
        String xmlData = "<root/>";

        InputStream xmlInput = new ByteArrayInputStream(xmlData.getBytes());
        List<String[]> rows = xmlToCSV(xmlInput);

        List<String[]> expected = List.of(new String[]{});
        assertEquals(expected.size(), rows.size());
    }
}