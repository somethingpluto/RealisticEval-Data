#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../adapted.cpp"
TEST_CASE("hexStringToUnsignedInt converts hex string to unsigned int", "[hexStringToUnsignedInt]") {

    SECTION("Valid hex strings") {
        REQUIRE(hexStringToUnsignedInt("1A3F") == 6719); // 1A3F in hex is 6719 in decimal
        REQUIRE(hexStringToUnsignedInt("FFFF") == 65535); // FFFF in hex is 65535 in decimal
        REQUIRE(hexStringToUnsignedInt("0") == 0); // 0 in hex is 0 in decimal
        REQUIRE(hexStringToUnsignedInt("7F") == 127); // 7F in hex is 127 in decimal
        REQUIRE(hexStringToUnsignedInt("ABC123") == 11256099); // ABC123 in hex is 11256099 in decimal
    }

    SECTION("Lowercase hex string") {
        REQUIRE(hexStringToUnsignedInt("abcd") == 43981); // abcd in hex is 43981 in decimal
    }

    SECTION("Hex string with leading zeroes") {
        REQUIRE(hexStringToUnsignedInt("0001") == 1); // 0001 in hex is 1 in decimal
    }

    SECTION("Empty hex string") {
        REQUIRE(hexStringToUnsignedInt("") == 0); // Empty string should be treated as 0
    }

    SECTION("Mixed case hex string") {
        REQUIRE(hexStringToUnsignedInt("AbCdEf") == 11259375); // AbCdEf in hex is 11259375 in decimal
    }
}