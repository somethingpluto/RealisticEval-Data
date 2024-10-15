TEST_CASE("compressHash") {
    SECTION("should return a string of length 5") {
        std::string hash = createHash("test");
        std::string result = compressHash(hash);
        REQUIRE(result.length() == 5);
    }

    SECTION("should return different strings for different inputs") {
        std::string hash1 = createHash("test1");
        std::string hash2 = createHash("test2");
        std::string result1 = compressHash(hash1);
        std::string result2 = compressHash(hash2);
        REQUIRE(result1 != result2);
    }

    SECTION("should return a consistent result for the same input") {
        std::string hash = createHash("test");
        std::string result1 = compressHash(hash);
        std::string result2 = compressHash(hash);
        REQUIRE(result1 == result2);
    }

    SECTION("should handle a hash of all zeros") {
        unsigned char zeroHash[32] = {0}; // 32 bytes of zeros
        std::string result = compressHash(std::string(reinterpret_cast<char*>(zeroHash), 32));
        REQUIRE(std::regex_match(result, std::regex("^[0-9a-zA-Z]{5}$")));
    }

    SECTION("should handle a hash of all ones") {
        unsigned char oneHash[32] = {255}; // 32 bytes of 0xFF (255 in decimal)
        std::string result = compressHash(std::string(reinterpret_cast<char*>(oneHash), 32));
        REQUIRE(std::regex_match(result, std::regex("^[0-9a-zA-Z]{5}$")));
    }
}