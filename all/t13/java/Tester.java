package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testStandardTable() {
        String mdTable = "| Header 1 | Header 2 | Header 3 |\n" +
                         "|----------|----------|----------|\n" +
                         "| Row1Col1 | Row1Col2 | Row1Col3 |\n" +
                         "| Row2Col1 | Row2Col2 | Row2Col3 |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2", "Header 3"},
            new String[]{"Row1Col1", "Row1Col2", "Row1Col3"},
            new String[]{"Row2Col1", "Row2Col2", "Row2Col3"}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }

    @Test
    public void testInconsistentColumns() {
        String mdTable = "| Header 1 | Header 2 |\n" +
                         "|----------|----------|\n" +
                         "| Row1     | Row1Col2 | ExtraCol |\n" +
                         "| Row2     |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2"},
            new String[]{"Row1", "Row1Col2", "ExtraCol"},
            new String[]{"Row2"}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }

    @Test
    public void testEmptyCells() {
        String mdTable = "| Header 1 | Header 2 | Header 3 |\n" +
                         "|----------|----------|----------|\n" +
                         "|          | Row1Col2 |          |\n" +
                         "| Row2Col1 |          | Row2Col3 |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2", "Header 3"},
            new String[]{"", "Row1Col2", ""},
            new String[]{"Row2Col1", "", "Row2Col3"}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }

    @Test
    public void testAllEmptyRows() {
        String mdTable = "| Header 1 | Header 2 | Header 3 |\n" +
                         "|----------|----------|----------|\n" +
                         "|          |          |          |\n" +
                         "|          |          |          |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2", "Header 3"},
            new String[]{"", "", ""},
            new String[]{"", "", ""}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }

    @Test
    public void testExcessiveWhitespace() {
        String mdTable = "|  Header 1  |  Header 2  |  Header 3  |\n" +
                         "|------------|------------|------------|\n" +
                         "|  Row1Col1  |  Row1Col2  |  Row1Col3  |\n" +
                         "|  Row2Col1  |  Row2Col2  |  Row2Col3  |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2", "Header 3"},
            new String[]{"Row1Col1", "Row1Col2", "Row1Col3"},
            new String[]{"Row2Col1", "Row2Col2", "Row2Col3"}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }
}package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertEquals;
import static org.real.temp.Answer.*;
import java.util.Arrays;
import java.util.List;

public class Tester {

    @Test
    public void testStandardTable() {
        String mdTable = "| Header 1 | Header 2 | Header 3 |\n" +
                         "|----------|----------|----------|\n" +
                         "| Row1Col1 | Row1Col2 | Row1Col3 |\n" +
                         "| Row2Col1 | Row2Col2 | Row2Col3 |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2", "Header 3"},
            new String[]{"Row1Col1", "Row1Col2", "Row1Col3"},
            new String[]{"Row2Col1", "Row2Col2", "Row2Col3"}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }

    @Test
    public void testInconsistentColumns() {
        String mdTable = "| Header 1 | Header 2 |\n" +
                         "|----------|----------|\n" +
                         "| Row1     | Row1Col2 | ExtraCol |\n" +
                         "| Row2     |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2"},
            new String[]{"Row1", "Row1Col2", "ExtraCol"},
            new String[]{"Row2"}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }

    @Test
    public void testEmptyCells() {
        String mdTable = "| Header 1 | Header 2 | Header 3 |\n" +
                         "|----------|----------|----------|\n" +
                         "|          | Row1Col2 |          |\n" +
                         "| Row2Col1 |          | Row2Col3 |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2", "Header 3"},
            new String[]{"", "Row1Col2", ""},
            new String[]{"Row2Col1", "", "Row2Col3"}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }

    @Test
    public void testAllEmptyRows() {
        String mdTable = "| Header 1 | Header 2 | Header 3 |\n" +
                         "|----------|----------|----------|\n" +
                         "|          |          |          |\n" +
                         "|          |          |          |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2", "Header 3"},
            new String[]{"", "", ""},
            new String[]{"", "", ""}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }

    @Test
    public void testExcessiveWhitespace() {
        String mdTable = "|  Header 1  |  Header 2  |  Header 3  |\n" +
                         "|------------|------------|------------|\n" +
                         "|  Row1Col1  |  Row1Col2  |  Row1Col3  |\n" +
                         "|  Row2Col1  |  Row2Col2  |  Row2Col3  |";

        List<String[]> expected = Arrays.asList(
            new String[]{"Header 1", "Header 2", "Header 3"},
            new String[]{"Row1Col1", "Row1Col2", "Row1Col3"},
            new String[]{"Row2Col1", "Row2Col2", "Row2Col3"}
        );

        List<String[]> result = parseMarkdownTable(mdTable);

        assertEquals(expected.size(), result.size());
        for (int i = 0; i < expected.size(); i++) {
            assertEquals(Arrays.asList(expected.get(i)), Arrays.asList(result.get(i)));
        }
    }
}