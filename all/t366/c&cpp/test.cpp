TEST_CASE("TestExtractTextFromWord", "[WordDocument]") {
    const std::string test_docx_path = "test_document.docx";

    SECTION("setUp") {
        // Helper method to create a sample Word document for testing
        void create_sample_docx(const std::string& docx_path, const std::vector<std::string>& paragraphs) {
            docx::Document doc;
            for (const auto& paragraph : paragraphs) {
                doc.add_paragraph(paragraph);
            }
            doc.save(docx_path);
        }

        // Set up the testing environment
        create_sample_docx(test_docx_path, {"Hello World!", "This is a test document."});
    }

    SECTION("tearDown") {
        // Clean up the test environment
        if (fs::exists(test_docx_path)) {
            fs::remove(test_docx_path);
        }
    }

    SECTION("test_extract_text_success") {
        // Test extracting text from a normal Word document
        const std::string expected_text = "Hello World!\nThis is a test document.";
        std::string extracted_text = extract_text_from_word(test_docx_path);
        REQUIRE(extracted_text == expected_text);
    }

    SECTION("test_extract_empty_document") {
        // Test extracting text from an empty Word document
        const std::string empty_docx_path = "empty_document.docx";
        docx::Document().save(empty_docx_path);

        std::string extracted_text = extract_text_from_word(empty_docx_path);
        REQUIRE(extracted_text.empty());

        if (fs::exists(empty_docx_path)) {
            fs::remove(empty_docx_path);
        }
    }

    SECTION("test_extract_text_with_special_characters") {
        // Test extracting text from a document containing special characters
        const std::string special_docx_path = "special_characters.docx";
        docx::Document doc;
        doc.add_paragraph("Hello, 世界! @#$%^&*()");
        doc.save(special_docx_path);

        std::string extracted_text = extract_text_from_word(special_docx_path);
        const std::string expected_text = "Hello, 世界! @#$%^&*()";
        REQUIRE(extracted_text == expected_text);

        if (fs::exists(special_docx_path)) {
            fs::remove(special_docx_path);
        }
    }

    SECTION("test_extract_text_with_multiple_paragraphs") {
        // Test extracting text from a document with multiple paragraphs
        const std::string multi_para_docx_path = "multi_paragraphs.docx";
        docx::Document doc;
        doc.add_paragraph("First paragraph.");
        doc.add_paragraph("Second paragraph.");
        doc.add_paragraph("Third paragraph.");
        doc.save(multi_para_docx_path);

        std::string extracted_text = extract_text_from_word(multi_para_docx_path);
        const std::string expected_text = "First paragraph.\nSecond paragraph.\nThird paragraph.";
        REQUIRE(extracted_text == expected_text);

        if (fs::exists(multi_para_docx_path)) {
            fs::remove(multi_para_docx_path);
        }
    }
}