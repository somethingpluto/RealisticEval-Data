TEST_CASE("Extract Text From Word", "[word]") {
    // Path to the test .docx file
    std::string docxFilePath = "path/to/your/test.docx";

    // Expected output
    std::string expectedOutput = "This is the expected text content.";

    // Actual output from the function
    std::string actualOutput = extractTextFromWord(docxFilePath);

    // Check if the actual output matches the expected output
    REQUIRE(actualOutput == expectedOutput);
}