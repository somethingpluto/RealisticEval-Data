TEST_CASE("Basic Indentation Test") {
    std::string code =
        "def example_function():\n"
        "print(\"Hello, world!\")\n"
        "if True:\n"
        "print(\"True branch\")\n"
        "else:\n"
        "print(\"False branch\")\n"
        "return\n";

    std::string expected =
        "def example_function():\n"
        "    print(\"Hello, world!\")\n"
        "    if True:\n"
        "        print(\"True branch\")\n"
        "    else:\n"
        "        print(\"False branch\")\n"
        "    return\n";

    std::string actual = fixIndentation(code);
    REQUIRE(actual == expected);
}

TEST_CASE("Empty Lines Test") {
    std::string code =
        "def example_function():\n"
        "\n"
        "print(\"Hello, world!\")\n"
        "\n"
        "if True:\n"
        "print(\"True branch\")\n"
        "return\n";

    std::string expected =
        "def example_function():\n"
        "\n"
        "    print(\"Hello, world!\")\n"
        "\n"
        "    if True:\n"
        "        print(\"True branch\")\n"
        "    return\n";

    std::string actual = fixIndentation(code);
    REQUIRE(actual == expected);
}

TEST_CASE("Multiple Statements Test") {
    std::string code =
        "def example_function():\n"
        "print(\"Hello, world!\")\n"
        "if True:\n"
        "print(\"True branch\")\n"
        "print(\"Still in True branch\")\n"
        "return\n";

    std::string expected =
        "def example_function():\n"
        "    print(\"Hello, world!\")\n"
        "    if True:\n"
        "        print(\"True branch\")\n"
        "        print(\"Still in True branch\")\n"
        "    return\n";

    std::string actual = fixIndentation(code);
    REQUIRE(actual == expected);
}

TEST_CASE("Nested Blocks Test") {
    std::string code =
        "def example_function():\n"
        "if True:\n"
        "if False:\n"
        "print(\"False branch\")\n"
        "else:\n"
        "print(\"Else branch\")\n"
        "return\n";

    std::string expected =
        "def example_function():\n"
        "    if True:\n"
        "        if False:\n"
        "            print(\"False branch\")\n"
        "        else:\n"
        "            print(\"Else branch\")\n"
        "        return\n";

    std::string actual = fixIndentation(code);
    REQUIRE(actual == expected);
}

TEST_CASE("No Indentation Needed Test") {
    std::string code =
        "def example_function():\n"
        "    print(\"Already correct\")\n"
        "    if True:\n"
        "        print(\"No change needed\")\n";

    std::string expected = code; // Already correctly indented

    std::string actual = fixIndentation(code);
    REQUIRE(actual == expected);
}