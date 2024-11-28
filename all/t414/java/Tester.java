package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.MockitoAnnotations;

import java.io.BufferedReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

import static org.mockito.Mockito.when;
import static org.junit.Assert.assertEquals;

@RunWith(MockitoJUnitRunner.class)
public class Tester {

    @Mock
    private BufferedReader mockReader;

    private static final String DUMMY_BIB_PATH = "dummy.bib";

    @Before
    public void setUp() throws IOException {
        MockitoAnnotations.initMocks(this);
        // Setup mock BufferedReader
        when(mockReader.readLine()).thenAnswer(invocation -> {
            String[] lines = getMockBibContent().split("\n");
            for (String line : lines) {
                if (line != null && !line.isEmpty()) {
                    return line;
                }
            }
            return null;
        });
    }

    @Test
    public void testValidEntry() throws IOException {
        String mockBib = "@article{sample2024,\n  author = {John Doe and Jane Smith},\n  title = {A Comprehensive Study on AI},\n  year = {2024}\n}";
        setMockBibContent(mockBib);

        List<Dictionary> result = extractBibInfo(DUMMY_BIB_PATH);
        List<Dictionary> expected = List.of(
            new Dictionary()
                .put("title", "A Comprehensive Study on AI")
                .put("author", "John Doe and Jane Smith")
                .put("year", "2024")
        );

        assertEquals(expected, result);
    }

    @Test
    public void testMultipleEntries() throws IOException {
        String mockBib = "@article{sample2024,\n  author = {John Doe},\n  title = {A Comprehensive Study on AI},\n  year = {2024}\n}\n" +
                         "@article{sample2023,\n  author = {Jane Smith},\n  title = {Deep Learning Techniques},\n  year = {2023}\n}";
        setMockBibContent(mockBib);

        List<Dictionary> result = extractBibInfo(DUMMY_BIB_PATH);
        List<Dictionary> expected = List.of(
            new Dictionary()
                .put("title", "A Comprehensive Study on AI")
                .put("author", "John Doe")
                .put("year", "2024"),
            new Dictionary()
                .put("title", "Deep Learning Techniques")
                .put("author", "Jane Smith")
                .put("year", "2023")
        );

        assertEquals(expected, result);
    }

    @Test
    public void testMissingFields() throws IOException {
        String mockBib = "@article{sample2024,\n  author = {John Doe},\n  title = {Title Missing Year}\n}";
        setMockBibContent(mockBib);

        List<Dictionary> result = extractBibInfo(DUMMY_BIB_PATH);
        List<Dictionary> expected = List.of(
            new Dictionary()
                .put("title", "Title Missing Year")
                .put("author", "John Doe")
                .put("year", null)
        );

        assertEquals(expected, result);
    }

    @Test
    public void testEmptyFile() throws IOException {
        String mockBib = "";
        setMockBibContent(mockBib);

        List<Dictionary> result = extractBibInfo(DUMMY_BIB_PATH);
        List<Dictionary> expected = List.of();

        assertEquals(expected, result);
    }

    @Test
    public void testIncorrectFormat() throws IOException {
        String mockBib = "@article{sample2024,\n  author = John Doe,\n  title = {Title Without Braces},\n  year = 2024\n}";
        setMockBibContent(mockBib);

        List<Dictionary> result = extractBibInfo(DUMMY_BIB_PATH);
        List<Dictionary> expected = List.of(
            new Dictionary()
                .put("title", "Title Without Braces")
                .put("author", null)
                .put("year", null)
        );

        assertEquals(expected, result);
    }

    private void setMockBibContent(String content) {
        when(mockReader.readLine()).thenAnswer(invocation -> {
            String[] lines = content.split("\n");
            for (String line : lines) {
                if (line != null && !line.isEmpty()) {
                    return line;
                }
            }
            return null;
        });
    }

    private List<Dictionary> extractBibInfo(String bibFile) {
        List<Dictionary> articles = new ArrayList<>();

        // Regular expressions to match title, author, and year
        Pattern titlePattern = Pattern.compile("title\\s*=\\s*{([^}]*)}", Pattern.CASE_INSENSITIVE);
        Pattern authorPattern = Pattern.compile("author\\s*=\\s*{([^}]*)}", Pattern.CASE_INSENSITIVE);
        Pattern yearPattern = Pattern.compile("year\\s*=\\s*{([^}]*)}", Pattern.CASE_INSENSITIVE);

        try (BufferedReader reader = mockReader) {
            StringBuilder content = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }

            // Split the content into individual entries based on '@'
            String[] entries = content.toString().split("@");

            // Skip the first split, which is empty
            for (int i = 1; i < entries.length; i++) {
                Matcher titleMatcher = titlePattern.matcher(entries[i]);
                Matcher authorMatcher = authorPattern.matcher(entries[i]);
                Matcher yearMatcher = yearPattern.matcher(entries[i]);

                Dictionary article = new Dictionary();

                if (titleMatcher.find()) {
                    article.put("title", titleMatcher.group(1));
                } else {
                    article.put("title", null);
                }

                if (authorMatcher.find()) {
                    article.put("author", authorMatcher.group(1));
                } else {
                    article.put("author", null);
                }

                if (yearMatcher.find()) {
                    article.put("year", yearMatcher.group(1));
                } else {
                    article.put("year", null);
                }

                articles.add(article);
            }

        } catch (IOException e) {
            System.out.println("Error: The file '" + bibFile + "' was not found.");
        }

        return articles;
    }

    /**
     * Simple implementation of a dictionary (key-value store).
     */
    public static class Dictionary {
        private final java.util.Map<String, String> map = new java.util.HashMap<>();

        /**
         * Puts a key-value pair into the dictionary.
         *
         * @param key   The key.
         * @param value The value.
         * @return This Dictionary instance for chaining.
         */
        public Dictionary put(String key, String value) {
            map.put(key, value);
            return this;
        }

        @Override
        public String toString() {
            return map.toString();
        }
    }
}
