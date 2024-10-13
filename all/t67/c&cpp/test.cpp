TEST_CASE("Test parse_xaml_to_dict", "[parse_xaml_to_dict]") {
    SECTION("test_valid_strings") {
        std::string xaml_data = R"(<root>
                                     <String Key="Username">Alice</String>
                                     <String Key="Password">secret</String>
                                   </root>)";
        std::map<std::string, std::string> expected = {{"Username", "Alice"}, {"Password", "secret"}};
        std::map<std::string, std::string> result = parse_xaml_to_dict(xaml_data);
        REQUIRE(result == expected);
    }

    SECTION("test_missing_key_attribute") {
        std::string xaml_data = R"(<root>
                                     <String>Alice</String>
                                   </root>)";
        std::map<std::string, std::string> expected = {};
        std::map<std::string, std::string> result = parse_xaml_to_dict(xaml_data);
        REQUIRE(result == expected);
    }

    SECTION("test_no_string_tags") {
        std::string xaml_data = R"(<root>
                                     <Data>Some question</Data>
                                   </root>)";
        std::map<std::string, std::string> expected = {};
        std::map<std::string, std::string> result = parse_xaml_to_dict(xaml_data);
        REQUIRE(result == expected);
    }

    SECTION("test_nested_string_tags") {
        std::string xaml_data = R"(<root>
                                     <Container>
                                       <String Key="Username">Bob</String>
                                     </Container>
                                     <String Key="Location">Earth</String>
                                   </root>)";
        std::map<std::string, std::string> expected = {{"Username", "Bob"}, {"Location", "Earth"}};
        std::map<std::string, std::string> result = parse_xaml_to_dict(xaml_data);
        REQUIRE(result == expected);
    }
}