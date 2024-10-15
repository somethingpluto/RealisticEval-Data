TEST_CASE("arrayBufferToString") {
    SECTION("should return an empty string for an empty buffer") {
        std::vector<uint8_t> buffer1;
        std::string result = arrayBufferToString(buffer1);
        REQUIRE(result == ""); // Expected: ""
    }

    SECTION("should return 'A' for a buffer containing the character 'A'") {
        std::vector<uint8_t> buffer2 = {'A'};
        std::string result = arrayBufferToString(buffer2);
        REQUIRE(result == "A"); // Expected: "A"
    }

    SECTION("should return 'Hello' for a buffer containing the string 'Hello'") {
        std::vector<uint8_t> buffer3 = {'H', 'e', 'l', 'l', 'o'};
        std::string result = arrayBufferToString(buffer3);
        REQUIRE(result == "Hello"); // Expected: "Hello"
    }

    SECTION("should return the correct string for a buffer containing multiple characters") {
        std::vector<uint8_t> buffer4 = {'H', 'e', 'l', 'l', 'o', ',', ' ', 'W', 'o', 'r', 'l', 'd', '!'};
        std::string result = arrayBufferToString(buffer4);
        REQUIRE(result == "Hello, World!"); // Expected: "Hello, World!"
    }

    SECTION("should not modify the input buffer") {
        std::string input = "Test input";
        std::vector<uint8_t> buffer8(input.begin(), input.end());
        arrayBufferToString(buffer8);
        std::string result(buffer8.begin(), buffer8.end());
        REQUIRE(result == input); // Check if the buffer content remains unchanged
    }
}