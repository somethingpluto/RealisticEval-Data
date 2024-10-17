#include <catch2/catch_test_macros.hpp>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>

TEST_CASE("TestWrapContentGenerator", "[wrap_content_generator]") {
    SECTION("test_empty_content") {
        std::vector<std::string> result;
        wrap_content_generator("", 80, [&result](const std::string &line) {
            result.push_back(line);
        });
        REQUIRE(result == std::vector<std::string>({"\n"}));
    }

    SECTION("test_single_line_content") {
        std::vector<std::string> result;
        wrap_content_generator("Hello, world!", 80, [&result](const std::string &line) {
            result.push_back(line);
        });
        REQUIRE(result == std::vector<std::string>({"Hello, world!"}));
    }

    SECTION("test_multi_line_content") {
        std::vector<std::string> result;
        std::string content = "Hello\nWorld\nPython";
        wrap_content_generator(content, 80, [&result](const std::string &line) {
            result.push_back(line);
        });
        REQUIRE(result == std::vector<std::string>({"Hello", "World", "Python"}));
    }

    SECTION("test_long_line") {
        std::vector<std::string> result;
        std::string content = "This is a very long line that should definitely be wrapped around the default width of 80 characters.";
        wrap_content_generator(content, 80, [&result](const std::string &line) {
            result.push_back(line);
        });
        REQUIRE(std::all_of(result.begin(), result.end(), [](const std::string &line) {
            return line.length() <= 80;
        }));
    }

    SECTION("test_custom_width") {
        std::vector<std::string> result;
        std::string content = "This is a test for custom width setting.";
        wrap_content_generator(content, 10, [&result](const std::string &line) {
            result.push_back(line);
        });
        REQUIRE(std::all_of(result.begin(), result.end(), [](const std::string &line) {
            return line.length() <= 10;
        }));
    }

    SECTION("test_only_whitespaces") {
        std::vector<std::string> result;
        wrap_content_generator("     ", 80, [&result](const std::string &line) {
            result.push_back(line);
        });
        REQUIRE(result == std::vector<std::string>({"\n"}));
    }
}