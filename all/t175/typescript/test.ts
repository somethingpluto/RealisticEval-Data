describe('Answer', () => {
    test('testBasicIndentation', () => {
        const code = 
            "def example_function():\n" +
            "print(\"Hello, world!\")\n" +
            "if True:\n" +
            "print(\"True branch\")\n" +
            "else:\n" +
            "print(\"False branch\")\n" +
            "return\n";

        const expected = 
            "def example_function():\n" +
            "    print(\"Hello, world!\")\n" +
            "    if True:\n" +
            "        print(\"True branch\")\n" +
            "    else:\n" +
            "        print(\"False branch\")\n" +
            "    return\n";

        const actual = fixIndentation(code);
        expect(actual).toBe(expected);
    });

    test('testEmptyLines', () => {
        const code = 
            "def example_function():\n" +
            "\n" +
            "print(\"Hello, world!\")\n" +
            "\n" +
            "if True:\n" +
            "print(\"True branch\")\n" +
            "return\n";

        const expected = 
            "def example_function():\n" +
            "\n" +
            "    print(\"Hello, world!\")\n" +
            "\n" +
            "    if True:\n" +
            "        print(\"True branch\")\n" +
            "    return\n";

        const actual = fixIndentation(code);
        expect(actual).toBe(expected);
    });

    test('testMultipleStatements', () => {
        const code = 
            "def example_function():\n" +
            "print(\"Hello, world!\")\n" +
            "if True:\n" +
            "print(\"True branch\")\n" +
            "print(\"Still in True branch\")\n" +
            "return\n";

        const expected = 
            "def example_function():\n" +
            "    print(\"Hello, world!\")\n" +
            "    if True:\n" +
            "        print(\"True branch\")\n" +
            "        print(\"Still in True branch\")\n" +
            "    return\n";

        const actual = fixIndentation(code);
        expect(actual).toBe(expected);
    });

    test('testNestedBlocks', () => {
        const code = 
            "def example_function():\n" +
            "if True:\n" +
            "if False:\n" +
            "print(\"False branch\")\n" +
            "else:\n" +
            "print(\"Else branch\")\n" +
            "return\n";

        const expected = 
            "def example_function():\n" +
            "    if True:\n" +
            "        if False:\n" +
            "            print(\"False branch\")\n" +
            "        else:\n" +
            "            print(\"Else branch\")\n" +
            "        return\n";

        const actual = fixIndentation(code);
        expect(actual).toBe(expected);
    });

    test('testNoIndentationNeeded', () => {
        const code = 
            "def example_function():\n" +
            "    print(\"Already correct\")\n" +
            "    if True:\n" +
            "        print(\"No change needed\")\n";

        const expected = code; // Already correctly indented

        const actual = fixIndentation(code);
        expect(actual).toBe(expected);
    });
});