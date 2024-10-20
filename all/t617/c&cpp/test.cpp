TEST_CASE("Tester", "[json]") {
    std::string path;

    SECTION("valid JSON") {
        std::string json_content = R"({"name": "John", "age": 30})";
        path = "temp_valid.json";

        std::ofstream temp_file(path);
        temp_file << json_content;
        temp_file.close();

        auto result = parse_json_file(path);
        REQUIRE(result.at("name") == "John");
        REQUIRE(result.at("age") == 30);

        std::remove(path.c_str()); // Clean up the temporary file
    }

    SECTION("empty JSON") {
        std::string json_content = R"({})";
        path = "temp_empty.json";

        std::ofstream temp_file(path);
        temp_file << json_content;
        temp_file.close();

        auto result = parse_json_file(path);
        REQUIRE(result.empty());

        std::remove(path.c_str()); // Clean up the temporary file
    }

    SECTION("null input") {
        REQUIRE_THROWS_AS(parse_json_file(nullptr), std::invalid_argument);
    }

    SECTION("non-JSON file") {
        std::string not_json_content = "Hello, World!";
        path = "temp_not_json.txt";

        std::ofstream temp_file(path);
        temp_file << not_json_content;
        temp_file.close();

        REQUIRE_THROWS_AS(parse_json_file(path), std::runtime_error);

        std::remove(path.c_str()); // Clean up the temporary file
    }

    SECTION("JSON with array") {
        std::string json_content = R"({"names": ["John", "Doe"]})";
        path = "temp_array.json";

        std::ofstream temp_file(path);
        temp_file << json_content;
        temp_file.close();

        auto result = parse_json_file(path);
        REQUIRE(result.find("names") != result.end());

        std::remove(path.c_str()); // Clean up the temporary file
    }
}