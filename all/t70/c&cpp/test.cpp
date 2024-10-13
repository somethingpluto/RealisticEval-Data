TEST_CASE("Test code_block_remover", "[code_block_remover]") {
    SECTION("Single code block") {
        std::string markdown = R"(
        This is a markdown with a code block.

        ```python
        print("Hello, World!")
        ```

        End of markdown.
        )";
        std::vector<std::string> expected = {"print(\"Hello, World!\")"};
        std::vector<std::string> result = code_block_remover(markdown);
        REQUIRE(result == expected);
    }

    SECTION("Multiple code blocks") {
        std::string markdown = R"(
        First code block:

        ```python
        print("Hello, World!")
        ```

        Second code block:

        ```javascript
        console.log("Hello, World!");
        )";
        std::vector<std::string> expected = {
            "print(\"Hello, World!\")",
            "console.log(\"Hello, World!\");"
        };
        std::vector<std::string> result = code_block_remover(markdown);
        REQUIRE(result == expected);
    }

    SECTION("No code block") {
        std::string markdown = R"(
        This markdown has no code blocks.

        Just some plain text.
        )";
        std::vector<std::string> expected = {};
        std::vector<std::string> result = code_block_remover(markdown);
        REQUIRE(result == expected);
    }

    SECTION("Empty code block") {
        std::string markdown = R"(
        Here is an empty code block:

        ```python
        ```

        End of markdown.
        )";
        std::vector<std::string> expected = {""};
        std::vector<std::string> result = code_block_remover(markdown);
        REQUIRE(result == expected);
    }

    SECTION("Malformed code block") {
        std::string markdown = R"(
        This code block is missing ending:

        ```python
        print("Hello, World!")

        And some more text.
        )";
        std::vector<std::string> expected = {};
        std::vector<std::string> result = code_block_remover(markdown);
        REQUIRE(result == expected);
    }
}