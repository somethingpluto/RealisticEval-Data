#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"

// 测试用例 1: 基本 JSON 提取
TEST_CASE("Basic JSON extraction", "[extract_json]") {
    std::string input = "Here is a JSON: {\"key\": \"value\"} with text.";
    std::string expected = "{\"key\": \"value\"}";
    REQUIRE(token_manager::extract_json(input) == expected);
}

// 测试用例 2: 嵌套大括号
TEST_CASE("Nested braces JSON extraction", "[extract_json]") {
    std::string input = "Prefix {\"outer\": {\"inner\": \"value\"}} Suffix";
    std::string expected = "{\"outer\": {\"inner\": \"value\"}}";
    REQUIRE(token_manager::extract_json(input) == expected);
}

// 测试用例 3: 没有大括号的输入
TEST_CASE("No braces in input", "[extract_json]") {
    std::string input = "No JSON here.";
    std::string expected = "";
    REQUIRE(token_manager::extract_json(input) == expected);
}

// 测试用例 4: 只有开头的 '{'
TEST_CASE("Only opening brace", "[extract_json]") {
    std::string input = "Starts with a brace { but no closing one.";
    std::string expected = "";
    REQUIRE(token_manager::extract_json(input) == expected);
}

// 测试用例 5: 只有结尾的 '}'
TEST_CASE("Only closing brace", "[extract_json]") {
    std::string input = "Ends with a brace } but no opening one.";
    std::string expected = "";
    REQUIRE(token_manager::extract_json(input) == expected);
}