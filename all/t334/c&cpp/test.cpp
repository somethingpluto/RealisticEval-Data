#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <iomanip>
#include <sstream>
#include <ctime>

std::tm calculateGoodFriday(int year); // Declaration of the function

std::string formatDate(const std::tm& date) {
    std::ostringstream oss;
    oss << std::put_time(&date, "%a %b %d %Y");
    return oss.str();
}

TEST_CASE("calculateGoodFriday", "[GoodFriday]") {
    SECTION("should correctly calculate Good Friday for 2024") {
        std::tm result = calculateGoodFriday(2024);
        REQUIRE(formatDate(result) == "Fri Mar 29 2024");
    }

    SECTION("should correctly calculate Good Friday for 2021") {
        std::tm result = calculateGoodFriday(2021);
        REQUIRE(formatDate(result) == "Fri Apr 02 2021");
    }

    SECTION("should correctly calculate Good Friday for 2000") {
        std::tm result = calculateGoodFriday(2000);
        REQUIRE(formatDate(result) == "Fri Apr 21 2000");
    }

    SECTION("should correctly calculate Good Friday for 2019") {
        std::tm result = calculateGoodFriday(2019);
        REQUIRE(formatDate(result) == "Fri Apr 19 2019");
    }

    SECTION("should correctly calculate Good Friday for 1999") {
        std::tm result = calculateGoodFriday(1999);
        REQUIRE(formatDate(result) == "Fri Apr 02 1999");
    }

    SECTION("should correctly calculate Good Friday for 1981") {
        std::tm result = calculateGoodFriday(1981);
        REQUIRE(formatDate(result) == "Fri Apr 17 1981");
    }

    SECTION("should correctly calculate Good Friday for 1954") {
        std::tm result = calculateGoodFriday(1954);
        REQUIRE(formatDate(result) == "Fri Apr 16 1954");
    }
}