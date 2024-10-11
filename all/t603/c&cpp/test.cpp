TEST_CASE("Leap Year Test Cases") {
    SECTION("Divisible by 4 but not by 100") {
        // Years that are leap years
        REQUIRE(isLeapYear(2024) == true); // 2024 is a leap year
        REQUIRE(isLeapYear(2000) == true); // 2000 is a leap year (divisible by 400)
        REQUIRE(isLeapYear(1996) == true); // 1996 is a leap year
        REQUIRE(isLeapYear(2004) == true); // 2004 is a leap year
    }

    SECTION("Divisible by 100 but not by 400") {
        // Years that are not leap years
        REQUIRE(isLeapYear(1900) == false); // 1900 is not a leap year
        REQUIRE(isLeapYear(2100) == false); // 2100 is not a leap year
        REQUIRE(isLeapYear(1800) == false); // 1800 is not a leap year
    }

    SECTION("Divisible by 400") {
        // Years that are leap years
        REQUIRE(isLeapYear(2400) == true); // 2400 is a leap year
        REQUIRE(isLeapYear(1600) == true); // 1600 is a leap year
    }

    SECTION("Normal years") {
        // Years that are normal years
        REQUIRE(isLeapYear(1997) == false); // 1997 is not a leap year
        REQUIRE(isLeapYear(1998) == false); // 1998 is not a leap year
        REQUIRE(isLeapYear(1999) == false); // 1999 is not a leap year
    }
}