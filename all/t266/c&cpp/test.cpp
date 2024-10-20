TEST_CASE("Test handle_nested_data function") {
    SECTION("Simple dictionary") {
        std::map<std::string, VarType> data = {{"name", std::string("Alice", 5)}, {"age", "30"}};
        std::map<std::string, VarType> expected = {{"name", "Alice"}, {"age", 30}};
        REQUIRE(handle_nested_data(data) == expected);
    }

    SECTION("Nested dictionary") {
        std::map<std::string, VarType> nestedData = {
            {"user", std::map<std::string, VarType>{{"name", std::string("Bob", 3)}, {"details", std::map<std::string, VarType>{{"age", "25"}, {"height", "175.5"}}}}}
        };
        std::map<std::string, VarType> expected = {
            {"user", std::map<std::string, VarType>{{"name", "Bob"}, {"details", std::map<std::string, VarType>{{"age", 25}, {"height", 175.5}}}}}
        };
        REQUIRE(handle_nested_data(nestedData) == expected);
    }

    SECTION("List of mixed data types") {
        std::vector<VarType> data = {"100", std::string("200", 3), 300.0, "400.5"};
        std::vector<VarType> expected = {100, std::string("200", 3), 300.0, 400.5};
        REQUIRE(handle_nested_data(data) == expected);
    }

    SECTION("Incorrect byte decoding") {
        std::map<std::string, VarType> data = {{"invalid_bytes", std::string("\xff\xfe\xfd\xfc", 4)}};
        REQUIRE_THROWS_AS(handle_nested_data(data), std::invalid_argument);
    }

    SECTION("Complex nested structure") {
        std::map<std::string, VarType> data = {
            {"team", std::vector<VarType>{
                std::map<std::string, VarType>{{"name", std::string("Charlie", 7)}, {"scores", std::vector<VarType>{"1000", "2000.2"}}},
                std::map<std::string, VarType>{{"name", std::string("Daisy", 5)}, {"skills", std::vector<VarType>{std::string("Coding", 6), "Design"}}, {"age", "22"}}
            }}
        };
        std::map<std::string, VarType> expected = {
            {"team", std::vector<VarType>{
                std::map<std::string, VarType>{{"name", "Charlie"}, {"scores", std::vector<VarType>{1000, 2000.2}}},
                std::map<std::string, VarType>{{"name", "Daisy"}, {"skills", std::vector<VarType>{"Coding", "Design"}}, {"age", 22}}
            }}
        };
        REQUIRE(handle_nested_data(data) == expected);
    }
}