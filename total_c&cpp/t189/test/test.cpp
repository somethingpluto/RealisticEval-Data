TEST_CASE("Base64 Encode Tests") {

    SECTION("Empty input should return empty string") {
        std::vector<unsigned char> input = {};
        REQUIRE(base64_encode(input) == "");
    }

    SECTION("Encoding 'hello' should return 'aGVsbG8='") {
        std::vector<unsigned char> input = {'h', 'e', 'l', 'l', 'o'};
        REQUIRE(base64_encode(input) == "aGVsbG8=");
    }

    SECTION("Encoding 'world' should return 'd29ybGQ='") {
        std::vector<unsigned char> input = {'w', 'o', 'r', 'l', 'd'};
        REQUIRE(base64_encode(input) == "d29ybGQ=");
    }

    SECTION("Encoding 'foobar' should return 'Zm9vYmFy'") {
        std::vector<unsigned char> input = {'f', 'o', 'o', 'b', 'a', 'r'};
        REQUIRE(base64_encode(input) == "Zm9vYmFy");
    }

    SECTION("Encoding 'Catch2' should return 'Q2F0Y2gy'") {
        std::vector<unsigned char> input = {'C', 'a', 't', 'c', 'h', '2'};
        REQUIRE(base64_encode(input) == "Q2F0Y2gy");
    }

    SECTION("Encoding single byte 'A' should return 'QQ=='") {
        std::vector<unsigned char> input = {'A'};
        REQUIRE(base64_encode(input) == "QQ==");
    }

}