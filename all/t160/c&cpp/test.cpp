TEST_CASE("compressFileName") {
    SECTION("should return the filename unchanged if under max length") {
        REQUIRE(compressFileName("file.txt", 10) == "file.txt");
    }

    SECTION("should truncate and append *** if filename exceeds max length") {
        REQUIRE(compressFileName("verylongfilename.txt", 10) == "verylongfi***.txt");
    }

    SECTION("should preserve file extension after compression") {
        REQUIRE(compressFileName("document.pdf", 5) == "docum***.pdf");
    }

    SECTION("should truncate and append *** if filename exceeds") {
        REQUIRE(compressFileName("short.mp3", 2) == "sh***.mp3");
    }
}