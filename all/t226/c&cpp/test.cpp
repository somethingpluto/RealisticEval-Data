TEST_CASE("TSV to JSONL Conversion", "[tsvToJsonl]") {
    // Create a temporary TSV file with some data
    std::ofstream tsvFile("temp.tsv");
    tsvFile << "name\tage\temail\n";
    tsvFile << "Alice\t30\talice@example.com\n";
    tsvFile << "Bob\t25\tbob@example.com\n";
    tsvFile.close();

    // Define the expected JSONL content
    std::string expectedJsonlContent = R"(
{
  "name": "Alice",
  "age": 30,
  "email": "alice@example.com"
}
{
  "name": "Bob",
  "age": 25,
  "email": "bob@example.com"
}
)";

    // Run the conversion
    std::string jsonlFile = "temp.jsonl";
    tsvToJsonl("temp.tsv", jsonlFile);

    // Read the generated JSONL file and compare its content with the expected content
    std::ifstream jsonlStream(jsonlFile);
    std::stringstream buffer;
    buffer << jsonlStream.rdbuf();
    std::string actualJsonlContent = buffer.str();

    REQUIRE(actualJsonlContent == expectedJsonlContent);

    // Clean up
    remove("temp.tsv");
    remove("temp.jsonl");
}