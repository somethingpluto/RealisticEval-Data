TEST_CASE("Test modular exponentiation", "[mod_exp]") {
    SECTION("Test with base = 2, exponent = 10, modulus = 1000") {
        REQUIRE(mod_exp(2, 10, 1000) == 24);
    }

    SECTION("Test with base = 3, exponent = 7, modulus = 50") {
        REQUIRE(mod_exp(3, 7, 50) == 37);
    }

    SECTION("Test with base = 5, exponent = 0, modulus = 13 (any number^0 = 1)") {
        REQUIRE(mod_exp(5, 0, 13) == 1);
    }

    SECTION("Test with base = 7, exponent = 5, modulus = 20") {
        REQUIRE(mod_exp(7, 5, 20) == 7);  // 7^5 = 16807, 16807 % 20 = 7
    }

    SECTION("Test with base = 10, exponent = 5, modulus = 6") {
        REQUIRE(mod_exp(10, 5, 6) == 4);  // 10^5 = 100000, 100000 % 6 = 4
    }
}