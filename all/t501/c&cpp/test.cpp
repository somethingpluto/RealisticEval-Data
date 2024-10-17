#include <iostream>
#include <string>
#include <sstream>
#include "catch.hpp"

// Test suite for the convert_to_short_format function
TEST_CASE("TestConvertToShortFormat", "[convert_to_short_format]") {
    SECTION("Test a standard input with mixed characters") {
        REQUIRE(convert_to_short_format("f1_p1_g1_b1_c1") == "fpgbc");
    }

    SECTION("Test input with multiple segments") {
        REQUIRE(convert_to_short_format("a2_b3_c4") == "abc");
    }

    SECTION("Test input with non-alphanumeric characters") {
        REQUIRE(convert_to_short_format("hello_world_test") == "hwt");
    }

    SECTION("Test a single segment input") {
        REQUIRE(convert_to_short_format("single") == "s");
    }
}