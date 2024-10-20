TEST_CASE("Test extraction from a badly formatted BibTeX entry", "[extract_bib_info]") {
    std::string mock_bib = R"(@article{sample2024,
  author = John Doe,
  title = {Title Without Braces},
  year = 2024
)}";

    std::istringstream mock_stream(mock_bib);
    std::vector<std::map<std::string, std::string>> result;
    {
        std::fstream file("dummy.bib");
        file.rdbuf(mock_stream.rdbuf());
        result = extract_bib_info("dummy.bib");
    }

    std::vector<std::map<std::string, std::string>> expected = {
        {{"title", "Title Without Braces"}, {"author", ""}, {"year", ""}}
    };

    REQUIRE(result == expected)}