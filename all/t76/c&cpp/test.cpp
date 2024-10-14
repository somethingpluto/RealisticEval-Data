TEST_CASE("Test remove_common_indentation function", "[remove_common_indentation]") {
    SECTION("test_empty_string") {
        // Testing edge case with an empty string
        CHECK(remove_common_indentation("") == "");
    }

    SECTION("test_single_line_string") {
        // Testing a single line with no indentation
        CHECK(remove_common_indentation("No indentation here") == "No indentation here");
    }

    SECTION("test_multiple_lines_with_uniform_indentation") {
        // Testing basic logic with uniform indentation across multiple lines
        std::string input_text = "    Line one\n    Line two\n    Line three";
        std::string expected_output = "Line one\nLine two\nLine three";
        CHECK(remove_common_indentation(input_text) == expected_output);
    }

    SECTION("test_multiple_lines_with_mixed_indentation") {
        // Testing lines with mixed indentation levels
        std::string input_text = "  Line one\n  Line two\n  Line three";
        std::string expected_output = "Line one\nLine two\nLine three";
        CHECK(remove_common_indentation(input_text) == expected_output);
    }
}