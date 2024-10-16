TEST_CASE("isPascalCase", "[PascalCase]") {
    REQUIRE(isPascalCase("PascalCase") == true);
    REQUIRE(isPascalCase("PascalCaseExample") == true);
    REQUIRE(isPascalCase("pascalCase") == false);
    REQUIRE(isPascalCase("Pascal_case") == false);
    REQUIRE(isPascalCase("") == false);
}