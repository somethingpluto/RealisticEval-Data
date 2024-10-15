TEST_CASE("isCppHeaderFile") {
    SECTION("returns true for a .h file") {
        REQUIRE(isCppHeaderFile("example.h") == true);
    }

    SECTION("returns true for a .hpp file") {
        REQUIRE(isCppHeaderFile("example.hpp") == true);
    }

    SECTION("returns false for a non-header file extension") {
        REQUIRE(isCppHeaderFile("example.txt") == false);
    }

    SECTION("returns false for a file without an extension") {
        REQUIRE(isCppHeaderFile("example") == false);
    }

    SECTION("returns false for a .c file") {
        REQUIRE(isCppHeaderFile("example.c") == false);
    }
}