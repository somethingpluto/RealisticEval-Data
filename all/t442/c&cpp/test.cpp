TEST_CASE("Test convert_strings_to_numbers") {
    SECTION("Convert dictionary") {
        std::map<std::string, std::variant<std::string, int, double>> input = {
            {"a", "123"},
            {"b", "456.789"},
            {"c", "not_a_number"}
        };
        auto output = convertStringsToNumbers(input);
        REQUIRE(std::holds_alternative<std::map<std::string, std::variant<std::string, int, double>>>(output));

        auto convertedMap = std::get<std::map<std::string, std::variant<std::string, int, double>>>(output);
        REQUIRE(convertedMap.size() == 3);

        REQUIRE(std::holds_alternative<int>(convertedMap.at("a")));
        REQUIRE(std::get<int>(convertedMap.at("a")) == 123);

        REQUIRE(std::holds_alternative<double>(convertedMap.at("b")));
        REQUIRE(std::get<double>(convertedMap.at("b")) == 456.789);

        REQUIRE(std::holds_alternative<std::string>(convertedMap.at("c")));
        REQUIRE(std::get<std::string>(convertedMap.at("c")) == "not_a_number");
    }

    SECTION("Convert list") {
        std::vector<std::variant<std::string, int, double>> input = {
            "123",
            "456.789",
            "not_a_number"
        };
        auto output = convertStringsToNumbers(input);
        REQUIRE(std::holds_alternative<std::vector<std::variant<std::string, int, double>>>(output));

        auto convertedVec = std::get<std::vector<std::variant<std::string, int, double>>>(output);
        REQUIRE(convertedVec.size() == 3);

        REQUIRE(std::holds_alternative<int>(convertedVec[0]));
        REQUIRE(std::get<int>(convertedVec[0]) == 123);

        REQUIRE(std::holds_alternative<double>(convertedVec[1]));
        REQUIRE(std::get<double>(convertedVec[1]) == 456.789);

        REQUIRE(std::holds_alternative<std::string>(convertedVec[2]));
        REQUIRE(std::get<std::string>(convertedVec[2]) == "not_a_number");
    }
}
