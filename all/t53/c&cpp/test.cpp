TEST_CASE("Test the size of various objects", "[size_in_bytes]") {
    SECTION("Test the size of an integer") {
        int integer_value = 42;
        size_t expected_size = sizeof(integer_value);
        size_t result_size = size_in_bytes(integer_value);
        REQUIRE(result_size == expected_size);
    }

    SECTION("Test the size of a string") {
        std::string string_value = "Hello, world!";
        size_t expected_size = sizeof(string_value);
        size_t result_size = size_in_bytes(string_value);
        REQUIRE(result_size == expected_size);
    }

    SECTION("Test the size of a list (vector)") {
        std::vector<int> list_value = {1, 2, 3, 4, 5};
        size_t expected_size = sizeof(list_value);
        size_t result_size = size_in_bytes(list_value);
        REQUIRE(result_size == expected_size);
    }

    SECTION("Test the size of a dictionary (map)") {
        std::map<std::string, std::string> dict_value = {{"key1", "value1"}, {"key2", "value2"}};
        size_t expected_size = sizeof(dict_value);
        size_t result_size = size_in_bytes(dict_value);
        REQUIRE(result_size == expected_size);
    }

    SECTION("Test the size of a custom object") {
        CustomObject custom_obj;
        size_t expected_size = sizeof(custom_obj);
        size_t result_size = size_in_bytes(custom_obj);
        REQUIRE(result_size == expected_size);
    }
}