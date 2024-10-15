#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>
#include <string>

std::string nextGreatestLetter(const std::vector<std::string>& letters, const std::string& target);

TEST_CASE("nextGreatestLetter") {
    SECTION("should return the first letter when target is greater than all letters in the array") {
        std::vector<std::string> letters = {"c", "f", "j"};
        std::string target = "j";
        std::string result = nextGreatestLetter(letters, target);
        REQUIRE(result == "c"); // Expected output: 'c'
    }

    SECTION("should return the next greatest letter for a typical input") {
        std::vector<std::string> letters = {"c", "f", "j"};
        std::string target = "a";
        std::string result = nextGreatestLetter(letters, target);
        REQUIRE(result == "c"); // Expected output: 'c'
    }

    SECTION("should handle the edge case where target is in between two letters") {
        std::vector<std::string> letters = {"c", "f", "j"};
        std::string target = "d";
        std::string result = nextGreatestLetter(letters, target);
        REQUIRE(result == "f"); // Expected output: 'f'
    }

    SECTION("should return the first letter when the target is equal to the largest letter") {
        std::vector<std::string> letters = {"a", "b", "c", "d"};
        std::string target = "d";
        std::string result = nextGreatestLetter(letters, target);
        REQUIRE(result == "a"); // Expected output: 'a'
    }

    SECTION("should return the correct letter when the array contains only one letter") {
        std::vector<std::string> letters = {"a"};
        std::string target = "z";
        std::string result = nextGreatestLetter(letters, target);
        REQUIRE(result == "a"); // Expected output: 'a'
    }
}