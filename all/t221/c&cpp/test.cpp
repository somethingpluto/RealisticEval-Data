TEST_CASE("Extract and Parse Dictionaries", "[file parsing]") {
    // Create a temporary file with some dictionary-like content
    std::ofstream tempFile;
    tempFile.open("temp_dict_file.txt");
    tempFile << "{ \"key1\": \"value1\", \"key2\": \"value2\" }\n";
    tempFile << "{ \"key3\": \"value3\", \"key4\": \"value4\" }\n";
    tempFile.close();

    // Call the function under test
    auto result = extract_parse_dicts("temp_dict_file.txt");

    // Check if the result contains the correct number of dictionaries
    REQUIRE(result.size() == 2);

    // Check if each dictionary is correctly parsed
    CHECK(result[0]["key1"] == "value1");
    CHECK(result[0]["key2"] == "value2");
    CHECK(result[1]["key3"] == "value3");
    CHECK(result[1]["key4"] == "value4");

    // Clean up the temporary file
    std::remove("temp_dict_file.txt");
}