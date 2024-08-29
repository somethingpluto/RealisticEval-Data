TEST_CASE("convFlags Test Cases", "[convFlags]") {
    // Test Case 1: All bits set
    REQUIRE(convFlags(0xFFFFFFFF) == "0");

    // Test Case 2: No bits set
    REQUIRE(convFlags(0x00000000) == "ffffffff");

    // Test Case 3: Random value (0xA5A5A5A5)
    REQUIRE(convFlags(0xA5A5A5A5) == "5a5a5a5a");

    // Test Case 4: Single bit set (0x80000000)
    REQUIRE(convFlags(0x80000000) == "7fffffff");

    // Test Case 5: Lower bits set (0x0000FFFF)
    REQUIRE(convFlags(0x0000FFFF) == "ffff0000");
}