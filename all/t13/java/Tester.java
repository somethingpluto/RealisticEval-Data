package org.real.temp;

import org.junit.Test;
import static org.junit.Assert.assertArrayEquals;

public class Tester {

    @Test
    public void testStandardTable() {
        String mdTable = """
            | Header 1 | Header 2 | Header 3 |
            |----------|----------|----------|
            | Row1Col1 | Row1Col2 | Row1Col3 |
            | Row2Col1 | Row2Col2 | Row2Col3 |
            """;

        Object[][] expected = {
            {"Header 1", "Header 2", "Header 3"},
            {"Row1Col1", "Row1Col2", "Row1Col3"},
            {"Row2Col1", "Row2Col2", "Row2Col3"}
        };

        Object[][] result = parseMarkdownTable(mdTable);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testInconsistentColumns() {
        String mdTable = """
            | Header 1 | Header 2 |
            |----------|----------|
            | Row1     | Row1Col2 | ExtraCol |
            | Row2     |
            """;

        Object[][] expected = {
            {"Header 1", "Header 2"},
            {"Row1", "Row1Col2", "ExtraCol"},
            {"Row2"}
        };

        Object[][] result = parseMarkdownTable(mdTable);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testEmptyCells() {
        String mdTable = """
            | Header 1 | Header 2 | Header 3 |
            |----------|----------|----------|
            |          | Row1Col2 |          |
            | Row2Col1 |          | Row2Col3 |
            """;

        Object[][] expected = {
            {"Header 1", "Header 2", "Header 3"},
            {"", "Row1Col2", ""},
            {"Row2Col1", "", "Row2Col3"}
        };

        Object[][] result = parseMarkdownTable(mdTable);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testAllEmptyRows() {
        String mdTable = """
            | Header 1 | Header 2 | Header 3 |
            |----------|----------|----------|
            |          |          |          |
            |          |          |          |
            """;

        Object[][] expected = {
            {"Header 1", "Header 2", "Header 3"},
            {"", "", ""},
            {"", "", ""}
        };

        Object[][] result = parseMarkdownTable(mdTable);
        assertArrayEquals(expected, result);
    }

    @Test
    public void testExcessiveWhitespace() {
        String mdTable = """
            |  Header 1  |  Header 2  |  Header 3  |
            |------------|------------|------------|
            |  Row1Col1  |  Row1Col2  |  Row1Col3  |
            |  Row2Col1  |  Row2Col2  |  Row2Col3  |
            """;

        Object[][] expected = {
            {"Header 1", "Header 2", "Header 3"},
            {"Row1Col1", "Row1Col2", "Row1Col3"},
            {"Row2Col1", "Row2Col2", "Row2Col3"}
        };

        Object[][] result = parseMarkdownTable(mdTable);
        assertArrayEquals(expected, result);
    }
}
