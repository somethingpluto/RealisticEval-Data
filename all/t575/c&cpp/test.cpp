TEST_CASE("formatThreadCount", "[formatThreadCount]") {
    REQUIRE(formatThreadCount(1) == "01 Thread");
    REQUIRE(formatThreadCount(5) == "05 Threads");
    REQUIRE(formatThreadCount(10) == "10 Threads");
    REQUIRE(formatThreadCount(99) == "99 Threads");
}