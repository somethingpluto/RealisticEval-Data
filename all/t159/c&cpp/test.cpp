TEST_CASE("removeFileExtension") {
    SECTION("should remove the file extension from a standard file") {
        REQUIRE(removeFileExtension("document.txt") == "document");
    }

    SECTION("should return the original filename for files without an extension") {
        REQUIRE(removeFileExtension("document") == "document");
    }

    SECTION("should handle files with multiple dots correctly") {
        REQUIRE(removeFileExtension("my.file.with.many.extensions.pdf") == "my.file.with.many.extensions");
    }

    SECTION("should return the original filename if it ends with a dot") {
        REQUIRE(removeFileExtension("document.") == "document");
    }

    SECTION("should correctly handle filenames with dots in directory names") {
        REQUIRE(removeFileExtension("path.to/my.file.txt") == "path.to/my.file");
    }
}