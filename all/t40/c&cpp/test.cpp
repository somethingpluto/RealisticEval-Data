#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>

// We have to declare or include the adjustToCMajor function here
std::string adjustToCMajor(const std::string& noteName); // assume this function is properly defined elsewhere

TEST_CASE("TestAdjustToCMajor") {
    SECTION("test_note_already_in_c_major") {
        REQUIRE(adjustToCMajor("C4") == "C4");
        REQUIRE(adjustToCMajor("G3") == "G3");
    }

    SECTION("test_note_not_in_c_major") {
        REQUIRE(adjustToCMajor("C#4") == "D4");
        REQUIRE(adjustToCMajor("F#3") == "G3");
    }

    SECTION("test_invalid_note_name") {
        REQUIRE(adjustToCMajor("H2") == "C4");
    }

    SECTION("test_edge_case_near_c_major") {
        REQUIRE(adjustToCMajor("B#3") == "C4");
        REQUIRE(adjustToCMajor("E#4") == "F4");
    }
}