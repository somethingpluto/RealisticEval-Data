TEST_CASE("Base64 Encoding Tests") {
    SECTION("Convert simple string to Base64") {
        REQUIRE(convertToBase64("Hello, World!") == "SGVsbG8sIFdvcmxkIQ==");
    }

    SECTION("Convert empty string to Base64") {
        REQUIRE(convertToBase64("") == "");
    }

    SECTION("Convert string with spaces to Base64") {
        REQUIRE(convertToBase64("Test String with Spaces") == "VGVzdCBTdHJpbmcgd2l0aCBTcGFjZXM=");
    }

    SECTION("Convert string with special characters to Base64") {
        REQUIRE(convertToBase64("Special characters: @#&*()") == "U3BlY2lhbCBjaGFyYWN0ZXJzOiBAIyYqKCk=");
    }

    SECTION("Convert string with non-ASCII characters to Base64") {
        REQUIRE(convertToBase64("你好，世界！") == "5L2g5aW977yM5LiW55WM77yB");
    }

    SECTION("Convert long string to Base64") {
        const std::string longString = "This is a very long string that exceeds normal lengths for testing purposes.";
        REQUIRE(convertToBase64(longString) == "VGhpcyBpcyBhIHZlcnkgbG9uZyBzdHJpbmcgdGhhdCBleGNlZWRzIG5vcm1hbCBsZW5ndGhzIGZvciB0ZXN0aW5nIHB1cnBvc2VzLg==");
    }
}