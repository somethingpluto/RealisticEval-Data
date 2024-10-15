#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>
#include <regex>

// Assume generateUUID() is defined elsewhere

TEST_CASE("generateUUID") {

    SECTION("should return a string") {
        std::string result = generateUUID();
        REQUIRE(!result.empty());
    }

    SECTION("should return a string of length 36") {
        std::string result = generateUUID();
        REQUIRE(result.length() == 36);
    }

    SECTION("should generate different UUIDs on consecutive calls") {
        std::string uuid1 = generateUUID();
        std::string uuid2 = generateUUID();
        REQUIRE(uuid1 != uuid2);
    }

    SECTION("should generate UUIDs that include uppercase") {
        std::string result = generateUUID();
        REQUIRE(std::regex_search(result, std::regex("[A-Z]"))); // At least one uppercase letter
    }

    SECTION("should generate UUIDs that include lowercase letters") {
        std::string result = generateUUID();
        REQUIRE(std::regex_search(result, std::regex("[a-z]"))); // At least one lowercase letter
    }

    SECTION("should generate UUIDs that include digits") {
        std::string result = generateUUID();
        REQUIRE(std::regex_search(result, std::regex("[0-9]"))); // At least one digit
    }
}