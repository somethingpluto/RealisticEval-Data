TEST_CASE("Test CamelCase to snake_case conversion", "[convert_camel_to_snake]") {
    SECTION("Basic conversion") {
        REQUIRE(convert_camel_to_snake("HelloWorld") == "hello_world");
    }

    SECTION("Multiple words") {
        REQUIRE(convert_camel_to_snake("ThisIsATest") == "this_is_a_test");
    }

    SECTION("With numbers") {
        REQUIRE(convert_camel_to_snake("ConvertThis123String") == "convert_this123_string");
    }

    SECTION("Leading uppercase") {
        REQUIRE(convert_camel_to_snake("PythonFunction") == "python_function");
    }

    SECTION("Empty string") {
        REQUIRE(convert_camel_to_snake("") == "");
    }
}