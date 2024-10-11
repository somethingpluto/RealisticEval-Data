TEST_CASE("renameFilePath", "[file-path]") {
    REQUIRE(renameFilePath("C:\\Users\\Username\\Documents\\example.txt") == "C:\\Users\\Username\\Documents\\example.txt");
    REQUIRE(renameFilePath("C:\\Users\\Username\\Documents\\example:file.txt") == "C:\\Users\\Username\\Documents\\example_file.txt");
    REQUIRE(renameFilePath("C:\\Users\\Username\\Documents\\file:with:colons.txt") == "C:\\Users\\Username\\Documents\\file_with_colons.txt");
    REQUIRE(renameFilePath("C:\\Users\\Username\\Documents\\no_colon_in_filename.txt") == "C:\\Users\\Username\\Documents\\no_colon_in_filename.txt");
}