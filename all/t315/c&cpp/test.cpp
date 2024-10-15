TEST_CASE("getFileIdFromUrl", "[getFileIdFromUrl]") {
    SECTION("should return the file ID when a valid URL with fileId is provided") {
        std::string url = "https://example.com/download?fileId=12345";
        REQUIRE(getFileIdFromUrl(url) == "12345");
    }

    SECTION("should return empty string when the fileId query parameter is missing") {
        std::string url = "https://example.com/download";
        REQUIRE(getFileIdFromUrl(url) == "");
    }

    SECTION("should return empty string when the fileId query parameter is empty") {
        std::string url = "https://example.com/download?fileId=";
        REQUIRE(getFileIdFromUrl(url) == "");
    }

    SECTION("should return the file ID for a malformed URL") {
        std::string url = "https://example.com/download?fileId=12345&otherParam";
        REQUIRE(getFileIdFromUrl(url) == "12345"); // Adjust this depending on your needs; the function should still work correctly.
    }
}