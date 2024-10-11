TEST_CASE("Extract Bib Info", "[bib]") {
    // Create a temporary BibTeX file content
    std::map<std::string, std::map<std::string, std::string>> entries = {
        {"sample2024", {{"author", "John Doe and Jane Smith"}, {"title", "A Comprehensive Study on AI"}, {"year", "2024"}}}
    };
    std::string bibFileContent = createBibFileContent(entries);

    // Write the content to a temporary file
    std::ofstream tempFile("temp.bib");
    tempFile << bibFileContent;
    tempFile.close();

    // Call the function to be tested
    std::vector<std::map<std::string, std::string>> result = extract_bib_info("temp.bib");

    // Clean up the temporary file
    remove("temp.bib");

    // Verify the results
    REQUIRE(result.size() == 1);
    REQUIRE(result[0]["title"] == "A Comprehensive Study on AI");
    REQUIRE(result[0]["author"] == "John Doe and Jane Smith");
    REQUIRE(result[0]["year"] == "2024");
}