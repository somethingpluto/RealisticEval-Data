TEST_CASE("bytesToSize") {
    SECTION("should convert bytes to KB correctly") {
        REQUIRE(bytesToSize(1024) == "1.00 KB");
        REQUIRE(bytesToSize(2048) == "2.00 KB");
    }

    SECTION("should convert bytes to MB correctly") {
        REQUIRE(bytesToSize(1048576) == "1.00 MB");
        REQUIRE(bytesToSize(2097152) == "2.00 MB");
    }

    SECTION("should convert bytes to GB correctly") {
        REQUIRE(bytesToSize(1073741824) == "1.00 GB");
        REQUIRE(bytesToSize(2147483648) == "2.00 GB");
    }

    SECTION("should convert bytes to TB correctly") {
        REQUIRE(bytesToSize(1099511627776) == "1.00 TB");
        REQUIRE(bytesToSize(2199023255552) == "2.00 TB");
    }
}