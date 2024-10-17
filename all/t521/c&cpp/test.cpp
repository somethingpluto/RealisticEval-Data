#include <catch2/catch_test_macros.hpp>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <regex>
#include <algorithm>

TEST_CASE("Test Word Filter Counter") {
    SECTION("Test Case 1") {
        std::string text = "go to the school.go to the park.";
        std::vector<std::string> filter_words = {"go", "to", "the", "school", "park", "play"};
        std::unordered_map<std::string, int> expected_output = {
            {"go", 2},
            {"to", 2},
            {"the", 2},
            {"school", 1},
            {"park", 1},
            {"play", 0}
        };

        REQUIRE(word_filter_counter(text, filter_words) == expected_output);
    }

    SECTION("Test Case 2") {
        std::string text = "This is a completely different sentence.";
        std::vector<std::string> filter_words = {"I'll", "go", "to", "the", "school", "park", "play"};
        std::unordered_map<std::string, int> expected_output = {
            {"I'll", 0},
            {"go", 0},
            {"to", 0},
            {"the", 0},
            {"school", 0},
            {"park", 0},
            {"play", 0}
        };

        REQUIRE(word_filter_counter(text, filter_words) == expected_output);
    }

    SECTION("Test Case 3") {
        std::string text = "I will not go to the school's park.";
        std::vector<std::string> filter_words = {"I", "will", "not", "go", "to", "the", "school's", "park"};
        std::unordered_map<std::string, int> expected_output = {
            {"I", 1},
            {"will", 1},
            {"not", 1},
            {"go", 1},
            {"to", 1},
            {"the", 1},
            {"school's", 1},
            {"park", 1}
        };

        REQUIRE(word_filter_counter(text, filter_words) == expected_output);
    }
}