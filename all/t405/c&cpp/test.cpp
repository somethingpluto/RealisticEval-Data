TEST_CASE("Remove parts of string", "[remove_parts_of_string]") {
    SECTION("Single string with mixed cases") {
        REQUIRE(remove_parts_of_string("1234AbCde5678") == "AbCde5678");
    }

    SECTION("String starting with uppercase letters") {
        REQUIRE(remove_parts_of_string("ABCDefg") == "Defg");
    }

    SECTION("String starting with lowercase letters") {
        REQUIRE(remove_parts_of_string("abcDefg") == "Defg");
    }

    SECTION("String with no uppercase letters") {
        REQUIRE(remove_parts_of_string("abcdefg") == "");
    }

    SECTION("String with no lowercase letters") {
        REQUIRE(remove_parts_of_string("ABCDEFG") == "");
    }

    SECTION("Empty string") {
        REQUIRE(remove_parts_of_string("") == "");
    }
}