TEST_CASE("convFlags Test Cases", "[convFlags]") {
    // Test Case 1: All bits set (0xFFFFFFFF)
    REQUIRE(convFlags(0xFFFFFFFF) == "ffffffe0");

    // Test Case 2: No bits set (0x00000000)
    REQUIRE(convFlags(0x00000000) == "1f");

    // Test Case 3: Inverting first five bits only (0x0000001F)
    REQUIRE(convFlags(0x0000001F) == "0");

    // Test Case 4: Inverting first five bits of a random value (0x00000015)
    REQUIRE(convFlags(0x00000015) == "a");

    // Test Case 5: Inverting first five bits of a large number (0xFFFFFFE0)
    REQUIRE(convFlags(0xFFFFFFE0) == "ffffffff");
}