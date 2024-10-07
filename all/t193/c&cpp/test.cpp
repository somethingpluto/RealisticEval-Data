TEST_CASE("convFlags Test Cases", "[convFlags]") {
    REQUIRE(convFlags(0x0000001F) == "FFFFFFE0");

    REQUIRE(convFlags(0x00000015) == "FFFFFFEA");

    REQUIRE(convFlags(0xFFFFFFFF) == "0");

    REQUIRE(convFlags(0x12345678) == "EDCBA987");

    REQUIRE(convFlags(0x00000001) == "FFFFFFFE");

    REQUIRE(convFlags(0x00000003) == "FFFFFFFC");

    REQUIRE(convFlags(0x00000008) == "FFFFFFF7");

    REQUIRE(convFlags(0xABCDEF01) == "543210FE");
}