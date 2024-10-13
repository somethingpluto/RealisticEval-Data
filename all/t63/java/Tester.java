package org.real.temp;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.assertEquals;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class Tester {

    private List<List<String>> data;
    private List<String> columns;

    @Before
    public void setUp() {
        // Create sample data and columns
        data = Arrays.asList(
            Arrays.asList("Alice", "25"),
            Arrays.asList("Bob", "30")
        );
        columns = Arrays.asList("Name", "Age");
    }

    @Test
    public void testDfToStr() throws IOException {
        // Test that the function writes the correct markdown to a file
        String expectedMarkdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    25 |\n| Bob    |    30 |";
        String result = dataframeToMarkdown(data, columns, "dummy_path.md");
        assertEquals(expectedMarkdown, result);
    }

    @Test
    public void testEmptyDataFrame() throws IOException {
        // Test how the function handles an empty DataFrame
        List<List<String>> emptyData = Arrays.asList();
        List<String> emptyColumns = Arrays.asList();
        String expectedMarkdown = "";
        String result = dataframeToMarkdown(emptyData, emptyColumns, "dummy_path.md");
        assertEquals(expectedMarkdown, result);
    }

    @Test
    public void testSingleRowDataFrame() throws IOException {
        // Test with a DataFrame that contains only one row
        List<List<String>> singleRowData = Arrays.asList(
            Arrays.asList("Alice", "30")
        );
        List<String> singleRowColumns = Arrays.asList("Name", "Age");
        String expectedMarkdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    30 |";
        String result = dataframeToMarkdown(singleRowData, singleRowColumns, "dummy_path.md");
        assertEquals(expectedMarkdown, result);
    }

    @Test
    public void testNonStringColumns() throws IOException {
        // Test with non-string question types in the DataFrame
        List<List<String>> nonStringData = Arrays.asList(
            Arrays.asList("Alice", "25", "5.5"),
            Arrays.asList("Bob", "30", "6.0")
        );
        List<String> nonStringColumns = Arrays.asList("Name", "Age", "Height");
        String expectedMarkdown = "| Name   |   Age |   Height |\n|:-------|------:|---------:|\n| Alice  |    25 |      5.5 |\n| Bob    |    30 |      6   |";
        String result = dataframeToMarkdown(nonStringData, nonStringColumns, "dummy_path.md");
        assertEquals(expectedMarkdown, result);
    }

    @Test
    public void testSpecialCharacters() throws IOException {
        // Test handling of special characters in DataFrame
        List<List<String>> specialCharsData = Arrays.asList(
            Arrays.asList("Alice", "Good@Work!"),
            Arrays.asList("Bob", "Excellent & Commendable")
        );
        List<String> specialCharsColumns = Arrays.asList("Name", "Comments");
        String expectedMarkdown = "| Name   | Comments                |\n|:-------|:------------------------|\n| Alice  | Good@Work!              |\n| Bob    | Excellent & Commendable |";
        String result = dataframeToMarkdown(specialCharsData, specialCharsColumns, "dummy_path.md");
        assertEquals(expectedMarkdown, result);
    }

    // Utility method to convert DataFrame to Markdown
    private String dataframeToMarkdown(List<List<String>> data, List<String> columns, String mdPath) {
        StringBuilder markdown = new StringBuilder();

        // Construct the header row
        markdown.append("| ").append(String.join(" | ", columns)).append(" |\n");

        // Construct the separator row
        String separator = "| " + String.join(" | ", new String[columns.size()]) + " |\n";
        separator = separator.replace(" ", "---");
        markdown.append(separator);

        // Build markdown table body
        for (List<String> row : data) {
            markdown.append("| ").append(String.join(" | ", row)).append(" |\n");
        }

        // Write markdown to file
        try (FileWriter writer = new FileWriter(mdPath)) {
            writer.write(markdown.toString());
        } catch (IOException e) {
            e.printStackTrace();
        }

        return markdown.toString();
    }
}