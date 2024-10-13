package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import javax.xml.parsers.DocumentBuilder;
import javax.xml.parsers.DocumentBuilderFactory;
import javax.xml.parsers.ParserConfigurationException;
import org.w3c.dom.Document;
import org.w3c.dom.Element;
import org.w3c.dom.NodeList;
import org.xml.sax.SAXException;
import java.io.ByteArrayInputStream;
import java.io.IOException;

public class Tester {

    @Test
    public void testValidStrings() {
        String xamlData = "<root>\n" +
                          "  <String Key=\"Username\">Alice</String>\n" +
                          "  <String Key=\"Password\">secret</String>\n" +
                          "</root>";
        Map<String, String> expected = new HashMap<>();
        expected.put("Username", "Alice");
        expected.put("Password", "secret");

        Map<String, String> result = parseXamlToDict(xamlData);
        assertEquals(expected, result);
    }

    @Test
    public void testMissingKeyAttribute() {
        String xamlData = "<root>\n" +
                          "  <String>Alice</String>\n" +
                          "</root>";
        Map<String, String> expected = new HashMap<>();

        Map<String, String> result = parseXamlToDict(xamlData);
        assertEquals(expected, result);
    }

    @Test
    public void testNoStringTags() {
        String xamlData = "<root>\n" +
                          "  <Data>Some question</Data>\n" +
                          "</root>";
        Map<String, String> expected = new HashMap<>();

        Map<String, String> result = parseXamlToDict(xamlData);
        assertEquals(expected, result);
    }

    @Test
    public void testNestedStringTags() {
        String xamlData = "<root>\n" +
                          "  <Container>\n" +
                          "    <String Key=\"Username\">Bob</String>\n" +
                          "  </Container>\n" +
                          "  <String Key=\"Location\">Earth</String>\n" +
                          "</root>";
        Map<String, String> expected = new HashMap<>();
        expected.put("Username", "Bob");
        expected.put("Location", "Earth");

        Map<String, String> result = parseXamlToDict(xamlData);
        assertEquals(expected, result);
    }
}