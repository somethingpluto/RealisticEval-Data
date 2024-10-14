#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>

// Assuming the validURL function is defined somewhere
bool validURL(const std::string& str);

TEST_CASE("validURL", "[url]") {
    SECTION("validates a standard HTTP URL") {
        std::string url = "http://www.example.com";
        REQUIRE(validURL(url) == true);
    }

    SECTION("validates a secure HTTPS URL") {
        std::string url = "https://www.example.com";
        REQUIRE(validURL(url) == true);
    }

    SECTION("rejects a malformed URL") {
        std::string url = "htp:/www.example.com";
        REQUIRE(validURL(url) == false);
    }
}