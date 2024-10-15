TEST_CASE("getFileExtension", "[extension]") {
    SECTION("should return the file extension for a standard file") {
        REQUIRE(getFileExtension("example.txt") == "txt");
    }

    SECTION("should return an empty string for files without an extension") {
        REQUIRE(getFileExtension("example") == "");
    }

    SECTION("should handle files with multiple dots") {
        REQUIRE(getFileExtension("example.with.many.dots.jpg") == "jpg");
    }

    SECTION("should return an empty string for filenames that end with a dot") {
        REQUIRE(getFileExtension("example.") == "");
    }

    SECTION("should correctly handle case sensitivity") {
        REQUIRE(getFileExtension("example.JPG") == "JPG");
    }
}