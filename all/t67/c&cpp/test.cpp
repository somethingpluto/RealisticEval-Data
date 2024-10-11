TEST_CASE("Test Parse XAML to Dictionary", "[parse_xaml_to_dict]") {
    std::string xaml_content = R"(
        <root>
            <String key="name">John</String>
            <String key="age">30</String>
        </root>
    )";

    std::unordered_map<std::string, std::string> expected_output = {
        {"name", "John"},
        {"age", "30"}
    };

    auto result = parse_xaml_to_dict("dummy_path");  // Assuming parse_xaml_to_dict returns a std::unordered_map

    REQUIRE(result == expected_output);
}