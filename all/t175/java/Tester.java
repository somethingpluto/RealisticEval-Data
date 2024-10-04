package org.real.temp;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.real.temp.*;

public class Tester {
    @Test
    public void testBasicIndentation() {
        String code =
                "def example_function():\n" +
                        "print(\"Hello, world!\")\n" +
                        "if True:\n" +
                        "print(\"True branch\")\n" +
                        "else:\n" +
                        "print(\"False branch\")\n" +
                        "return\n";

        String expected =
                "def example_function():\n" +
                        "    print(\"Hello, world!\")\n" +
                        "    if True:\n" +
                        "        print(\"True branch\")\n" +
                        "    else:\n" +
                        "        print(\"False branch\")\n" +
                        "    return\n";

        String actual = Answer.fixIndentation(code);
        assertEquals(expected, actual);
    }

    @Test
    public void testEmptyLines() {
        String code =
                "def example_function():\n" +
                        "\n" +
                        "print(\"Hello, world!\")\n" +
                        "\n" +
                        "if True:\n" +
                        "print(\"True branch\")\n" +
                        "return\n";

        String expected =
                "def example_function():\n" +
                        "\n" +
                        "    print(\"Hello, world!\")\n" +
                        "\n" +
                        "    if True:\n" +
                        "        print(\"True branch\")\n" +
                        "    return\n";

        String actual = Answer.fixIndentation(code);
        assertEquals(expected, actual);
    }

    @Test
    public void testMultipleStatements() {
        String code =
                "def example_function():\n" +
                        "print(\"Hello, world!\")\n" +
                        "if True:\n" +
                        "print(\"True branch\")\n" +
                        "print(\"Still in True branch\")\n" +
                        "return\n";

        String expected =
                "def example_function():\n" +
                        "    print(\"Hello, world!\")\n" +
                        "    if True:\n" +
                        "        print(\"True branch\")\n" +
                        "        print(\"Still in True branch\")\n" +
                        "    return\n";

        String actual = Answer.fixIndentation(code);
        assertEquals(expected, actual);
    }

    @Test
    public void testNestedBlocks() {
        String code =
                "def example_function():\n" +
                        "if True:\n" +
                        "if False:\n" +
                        "print(\"False branch\")\n" +
                        "else:\n" +
                        "print(\"Else branch\")\n" +
                        "return\n";

        String expected =
                "def example_function():\n" +
                        "    if True:\n" +
                        "        if False:\n" +
                        "            print(\"False branch\")\n" +
                        "        else:\n" +
                        "            print(\"Else branch\")\n" +
                        "        return\n";

        String actual = Answer.fixIndentation(code);
        assertEquals(expected, actual);
    }

    @Test
    public void testNoIndentationNeeded() {
        String code =
                "def example_function():\n" +
                        "    print(\"Already correct\")\n" +
                        "    if True:\n" +
                        "        print(\"No change needed\")\n";

        String expected = code; // Already correctly indented

        String actual = Answer.fixIndentation(code);
        assertEquals(expected, actual);
    }
}
