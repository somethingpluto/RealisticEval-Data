TEST_CASE("code_block_remover tests", "[code_block_remover]") {
    SECTION("Empty markdown string") {
        REQUIRE(code_block_remover("") == std::vector<std::string>());
    }

    SECTION("Markdown with no code blocks") {
        REQUIRE(code_block_remover("This is some text without any code blocks.") == std::vector<std::string>());
    }

    SECTION("Markdown with one code block") {
        std::vector<std::string> expected = {"This is a code block."};
        REQUIRE(code_block_remover("Some text before\n```\nThis is a code block.\n```") == expected);
    }

    SECTION("Markdown with multiple code blocks") {
        std::vector<std::string> expected = {"This is the first code block.", "This is the second code block."};
        REQUIRE(code_block_remover("Some text before\n```\nThis is the first code block.\n```\nAnd here is another one:\n```\nThis is the second code block.\n```") == expected);
    }

    SECTION("Markdown with code blocks separated by other elements") {
        std::vector<std::string> expected = {"This is the first code block.", "This is the second code block."};
        REQUIRE(code_block_remover("Some text before\n```\nThis is the first code block.\n```\nMore text in between\n```\nThis is the second code block.\n```") == expected);
    }
}