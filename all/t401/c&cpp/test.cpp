TEST_CASE("Find Placeholders", "[find_placeholders]") {
    SECTION("Empty String") {
        std::string text = "";
        std::vector<std::string> expected = {};
        REQUIRE(find_placeholders(text) == expected);
    }

    SECTION("No Placeholders") {
        std::string text = "This is a normal sentence.";
        std::vector<std::string> expected = {};
        REQUIRE(find_placeholders(text) == expected);
    }

    SECTION("Single Placeholder") {
        std::string text = "{{ user_name }}";
        std::vector<std::string> expected = {"user_name"};
        REQUIRE(find_placeholders(text) == expected);
    }

    SECTION("Multiple Placeholders") {
        std::string text = "{{ user_name }} and {{ age }} years old.";
        std::vector<std::string> expected = {"user_name", "age"};
        REQUIRE(find_placeholders(text) == expected);
    }

    SECTION("Placeholders with Spaces") {
        std::string text = "{{ full name }}";
        std::vector<std::string> expected = {"full name"};
        REQUIRE(find_placeholders(text) == expected);
    }
}