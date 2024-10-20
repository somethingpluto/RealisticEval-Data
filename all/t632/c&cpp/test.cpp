TEST_CASE("Parser Tests") {
    SECTION("Simple Addition") {
        std::string expression = "2 + 2";
        auto result = parse_expression(expression);
        REQUIRE(result == std::vector<std::string>{"2", "+", "2"});
    }

    SECTION("Complex Expression") {
        std::string expression = "3 + 5 * (2 - 8)";
        auto result = parse_expression(expression);
        REQUIRE(result == std::vector<std::string>{"3", "+", "5", "*", "(", "2", "-", "8", ")"});
    }

    SECTION("Negative Numbers") {
        std::string expression = "-1 + 4 - 5";
        auto result = parse_expression(expression);
        REQUIRE(result == std::vector<std::string>{"-", "1", "+", "4", "-", "5"});
    }

    SECTION("Decimals") {
        std::string expression = "3.5 + 2.1";
        auto result = parse_expression(expression);
        REQUIRE(result == std::vector<std::string>{"3.5", "+", "2.1"});
    }

    SECTION("Operators Only") {
        std::string expression = "+ - * /";
        auto result = parse_expression(expression);
        REQUIRE(result == std::vector<std::string>{"+", "-", "*", "/"});
    }

    SECTION("Empty Expression") {
        std::string expression = "";
        auto result = parse_expression(expression);
        REQUIRE(result.empty());
    }

    SECTION("Single Number") {
        std::string expression = "42";
        auto result = parse_expression(expression);
        REQUIRE(result == std::vector<std::string>{"42"});
    }
}