#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>
#include <vector>
#include <map>

template <typename T>
size_t size_in_bytes(const T& obj) {
    return sizeof(obj);
}

TEST_CASE("Test size of integer") {
    int integer_value = 42;
    size_t expected_size = sizeof(integer_value);
    size_t result_size = size_in_bytes(integer_value);

    REQUIRE(result_size == expected_size);
}

TEST_CASE("Test size of string") {
    std::string string_value = "Hello, world!";
    size_t expected_size = sizeof(string_value); // Fixed part of the string object
    size_t result_size = size_in_bytes(string_value);

    REQUIRE(result_size == expected_size);
}

TEST_CASE("Test size of list") { // C++ equivalent: vector
    std::vector<int> list_value = {1, 2, 3, 4, 5};
    size_t expected_size = sizeof(list_value); // Fixed part of the vector object
    size_t result_size = size_in_bytes(list_value);

    REQUIRE(result_size == expected_size);
}

TEST_CASE("Test size of dictionary") { // C++ equivalent: map
    std::map<std::string, std::string> dict_value = {{"key1", "value1"}, {"key2", "value2"}};
    size_t expected_size = sizeof(dict_value); // Fixed part of the map object
    size_t result_size = size_in_bytes(dict_value);

    REQUIRE(result_size == expected_size);
}

class CustomObject {
public:
    char attr1;
    int attr2;

    CustomObject() : attr1('a'), attr2(123) {}
};

TEST_CASE("Test size of custom object") {
    CustomObject custom_obj;
    size_t expected_size = sizeof(custom_obj);
    size_t result_size = size_in_bytes(custom_obj);

    REQUIRE(result_size == expected_size);
}