TEST_CASE("isCamelCase") {
    SECTION("should return true for a valid camelCase string") {
        REQUIRE(isCamelCase("camelCase") == true);
    }

    SECTION("should return true for a valid camelCase string with multiple words") {
        REQUIRE(isCamelCase("camelCaseExample") == true);
    }

    SECTION("should return false for a string that starts with an uppercase letter") {
        REQUIRE(isCamelCase("CamelCase") == false);
    }

    SECTION("should return false for a string with underscores") {
        REQUIRE(isCamelCase("camel_case") == false);
    }

    SECTION("should return false for an empty string") {
        REQUIRE(isCamelCase("") == false);
    }
}