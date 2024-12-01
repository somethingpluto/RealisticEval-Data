TEST_CASE("Test move_emojis_to_end function") {
    SECTION("No emojis") {
        // Case: String with no emojis
        std::string input_text = "This is a test.";
        std::string expected_output = "This is a test.";
        REQUIRE(move_emojis_to_end(input_text) == expected_output);
    }

    SECTION("All emojis") {
        // Case: String with only emojis
        std::string input_text = "😀😃😄😁";
        std::string expected_output = "😀😃😄😁";
        REQUIRE(move_emojis_to_end(input_text) == expected_output);
    }

    SECTION("Emojis at the start") {
        // Case: Emojis at the start of the text
        std::string input_text = "😀😃Hello world!";
        std::string expected_output = "Hello world!😀😃";
        REQUIRE(move_emojis_to_end(input_text) == expected_output);
    }

    SECTION("Emojis at the end") {
        // Case: Emojis already at the end of the text
        std::string input_text = "Hello world!😀😃";
        std::string expected_output = "Hello world!😀😃";
        REQUIRE(move_emojis_to_end(input_text) == expected_output);
    }

    SECTION("Emojis in the middle") {
        // Case: Emojis in the middle of the text
        std::string input_text = "Hello 😀world😃!";
        std::string expected_output = "Hello world!😀😃";
        REQUIRE(move_emojis_to_end(input_text) == expected_output);
    }

    SECTION("Mixed characters") {
        // Case: Text with mixed characters and emojis
        std::string input_text = "Hi! 😀 How are you? 😃";
        std::string expected_output = "Hi!  How are you? 😀😃";
        REQUIRE(move_emojis_to_end(input_text) == expected_output);
    }
}