TEST_CASE("TestExtractTextFromPDF", "[PDF]") {
    SECTION("test_empty_file") {
        std::string pdf_path = R"(E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase01.pdf)";
        std::string expected = " \n";
        std::string output = extract_text_from_pdf(pdf_path);
        REQUIRE(output == expected);
    }

    SECTION("test_normal_file") {
        std::string pdf_path = R"(E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase02.pdf)";
        std::string expected = "11111  \n";
        std::string output = extract_text_from_pdf(pdf_path);
        REQUIRE(output == expected);
    }

    SECTION("test_more_text_file") {
        std::string pdf_path = R"(E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t249\testcase03.pdf)";
        std::string expected = "11111  \n22222  \n33333  \n44444  \n";
        std::string output = extract_text_from_pdf(pdf_path);
        REQUIRE(output == expected);
    }
}