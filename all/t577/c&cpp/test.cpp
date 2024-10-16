TEST_CASE("formatPostCount", "[formatPostCount]") {
    REQUIRE(formatPostCount(1) == "01 Post");
    REQUIRE(formatPostCount(2) == "02 Posts");
    REQUIRE(formatPostCount(10) == "10 Posts");
    REQUIRE(formatPostCount(99) == "99 Posts");
    REQUIRE(formatPostCount(5) == "05 Posts");
}