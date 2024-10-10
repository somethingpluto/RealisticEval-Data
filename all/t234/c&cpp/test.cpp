TEST_CASE("append_or_skip_row", "[csv]") {
    // Create a temporary CSV file with some initial data
    std::ofstream tempFile("temp.csv");
    tempFile << "col1,col2,col3,col4\n";
    tempFile << "value1,value2,value3,value4\n";
    tempFile.close();

    // Open the file in read-plus mode
    std::fstream fileHandler("temp.csv", std::ios::in | std::ios::out);
    REQUIRE(fileHandler.is_open());

    // Read the existing rows into a vector
    std::vector<std::string> rows;
    std::string line;
    while (std::getline(reader, line)) {
        rows.push_back(line);
    }

    // Define the candidate row to append
    std::vector<std::string> rowCandidate = {"value5", "value6", "value7", "value8"};

    // Call the function under test
    append_or_skip_row(fileHandler, reader, rowCandidate);

    // Seek back to the beginning of the file to read the updated content
    fileHandler.seekg(0, std::ios::beg);
    std::stringstream ss;
    ss << fileHandler.rdbuf();
    std::string updatedContent = ss.str();

    // Check that the candidate row was appended
    REQUIRE(updatedContent.find("value5,value6,value7,value8") != std::string::npos);

    // Clean up
    fileHandler.close();
    std::remove("temp.csv");
}