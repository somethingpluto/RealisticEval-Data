TEST_CASE("base64ToArrayBuffer function", "[base64]") {
    // Test Case 1
    SECTION("should decode 'SGVsbG8sIFdvcmxkIQ==' to 'Hello, World!'") {
        std::string base64 = "SGVsbG8sIFdvcmxkIQ==";
        std::string expected = "Hello, World!";
        auto arrayBuffer = base64ToArrayBuffer(base64);
        std::string result = bytesToString(arrayBuffer);
        REQUIRE(result == expected);
    }

    // Test Case 2
    SECTION("should decode 'U29tZSB0ZXh0IHdpdGggc3BhcmluZyBhbmQgd29ya2luZyE=' to 'Some text with sparing and working!'") {
        std::string base64 = "U29tZSB0ZXh0IHdpdGggc3BhcmluZyBhbmQgd29ya2luZyE=";
        std::string expected = "Some text with sparing and working!";
        auto arrayBuffer = base64ToArrayBuffer(base64);
        std::string result = bytesToString(arrayBuffer);
        REQUIRE(result == expected);
    }

    // Test Case 3
    SECTION("should decode 'QmFzZTY0IGVuY29kaW5nIGlzIGEgY29tbW9ubG9nIEZvciBiaW5hcnkgZGF0YQ==' to 'Base64 encoding is a common log For binary data'") {
        std::string base64 = "QmFzZTY0IGVuY29kaW5nIGlzIGEgY29tbW9ubG9nIEZvciBiaW5hcnkgZGF0YQ==";
        std::string expected = "Base64 encoding is a common log For binary data";
        auto arrayBuffer = base64ToArrayBuffer(base64);
        std::string result = bytesToString(arrayBuffer);
        REQUIRE(result == expected);
    }

    // Test Case 4
    SECTION("should decode 'R2l2ZSBtZSBhbG9uZyBhIHBhdGggdG8gY29tcGxldGUgc3RhcnQgcGFnZS4=' to 'Give me along a path to complete start page.'") {
        std::string base64 = "R2l2ZSBtZSBhbG9uZyBhIHBhdGggdG8gY29tcGxldGUgc3RhcnQgcGFnZS4=";
        std::string expected = "Give me along a path to complete start page.";
        auto arrayBuffer = base64ToArrayBuffer(base64);
        std::string result = bytesToString(arrayBuffer);
        REQUIRE(result == expected);
    }
}