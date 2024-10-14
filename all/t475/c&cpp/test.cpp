#include <catch2/catch.hpp>
#include <string>

std::string safe_format(const std::string& template_str, const std::map<std::string, std::string>& kwargs) {
    std::string result = template_str;
    for (const auto& kv : kwargs) {
        size_t pos = 0;
        while ((pos = result.find("{" + kv.first + "}", pos)) != std::string::npos) {
            result.replace(pos, kv.first.size() + 2, kv.second);
            pos += kv.second.size();
        }
    }
    return result;
}

TEST_CASE("Test Safe Format", "[safe_format]") {
    REQUIRE(safe_format("Hello, {name}!", {{"name", "Alice"}}) == "Hello, Alice!");
    REQUIRE(safe_format("Hello, {name}!", {{"age", "30"}}) == "Hello, {name}!");
    REQUIRE(safe_format("{greeting}, {name}! How old are you?", {{"greeting", "Hi"}, {"name", "Bob"}, {"age", "30"}}) == "Hi, Bob! How old are you?");
    REQUIRE(safe_format("{greeting}, {name}! How old are you?", {{"greeting", "Hi"}}) == "{greeting}, {name}! How old are you?");
}
