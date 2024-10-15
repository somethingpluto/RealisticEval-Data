#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>

// Assuming base64ToUrlSafe is defined somewhere
std::string base64ToUrlSafe(const std::string& base64);

TEST_CASE("base64ToUrlSafe") {

    SECTION("should correctly convert a standard Base64 string to URL-safe format") {
        std::string base64 = "YW55IGNhcm5hbCBwbGVhc3VyZS4+/w==";
        std::string result = base64ToUrlSafe(base64);
        REQUIRE(result == "YW55IGNhcm5hbCBwbGVhc3VyZS4-_w");
    }

    SECTION("should return an empty string when the input is an empty string") {
        std::string base64 = "";
        std::string result = base64ToUrlSafe(base64);
        REQUIRE(result == "");
    }

    SECTION("should remove only the trailing '=' characters") {
        std::string base64 = "dGVzdA==";
        std::string result = base64ToUrlSafe(base64);
        REQUIRE(result == "dGVzdA");
    }

    SECTION("should handle strings without any characters that need replacement") {
        std::string base64 = "dGVzdA";
        std::string result = base64ToUrlSafe(base64);
        REQUIRE(result == "dGVzdA");
    }

    SECTION("should handle a base64 string with multiple '+' and '/' characters") {
        std::string base64 = "aGVsbG8rL3dvcmxkLw==";
        std::string result = base64ToUrlSafe(base64);
        REQUIRE(result == "aGVsbG8rL3dvcmxkLw");
    }

    SECTION("should throw an error when input is not a string") {
        // Catch2 doesn't directly support throwing for invalid input types,
        // so this section might be omitted or adjusted for your use case.
        REQUIRE_THROWS_AS(base64ToUrlSafe(nullptr), std::invalid_argument);
    }
}