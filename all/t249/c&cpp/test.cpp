TEST_CASE("Extract Text From PDF", "[pdf]") {
    std::string file_path = "test.pdf";
    std::string expected_text = "This is a test PDF.";

    std::string result = extract_text_from_pdf(file_path);

    REQUIRE(result == expected_text);
}