TEST_CASE("Test Handle Nested Data", "[handle_nested_data]") {
    std::map<std::string, std::any> input_data = {
        {"key1", "value1"},
        {"key2", 123},
        {"key3", std::vector<std::string>{"value2", "value3"}},
        {"key4", std::map<std::string, std::string>{{"subkey1", "value4"}}}
    };

    std::map<std::string, std::any> expected_output = {
        {"key1", "value1"},
        {"key2", 123},
        {"key3", std::vector<std::string>{"value2", "value3"}},
        {"key4", std::map<std::string, std::string>{{"subkey1", "value4"}}}
    };

    std::map<std::string, std::any> output = handle_nested_data(input_data);

    REQUIRE(output == expected_output);
}