// Include the Catch2 header
#define CATCH_CONFIG_MAIN
#include "catch.hpp"
#include <string>

std::string convert_to_comma_separated(const std::string& input_string) {
    std::regex pattern("[\\*;/\\-\\:]");  
    std::string comma_separated_string = std::regex_replace(input_string, pattern, ",");
    return comma_separated_string;
}

TEST_CASE("convert_to_comma_separated") {
    SECTION("Basic Separators") {
        REQUIRE(convert_to_comma_separated("apple;banana*orange/mango") == "apple,banana,orange,mango");
    }

    SECTION("Mixed Separators") {
        REQUIRE(convert_to_comma_separated("grapes;lemon/melon*kiwi;litchi") == "grapes,lemon,melon,kiwi,litchi");
    }

    SECTION("No Separators") {
        REQUIRE(convert_to_comma_separated("watermelon") == "watermelon");
    }
    
    SECTION("Repeated Separators") {
        REQUIRE(convert_to_comma_separated("pear;;apple**banana//orange") == "pear,,apple,,banana,,orange");
    }
}