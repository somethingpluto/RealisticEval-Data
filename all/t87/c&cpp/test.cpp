TEST_CASE("timestampToReadableDate", "[timestamp]") {
    SECTION("should convert UNIX timestamp to readable format") {
        long long timestamp = 1696516800;
        REQUIRE(timestampToReadableDate(timestamp) == "Oct 5, 22:40");
    }

    SECTION("should handle timestamp at the start of the year") {
        long long timestamp = 1672531200;
        REQUIRE(timestampToReadableDate(timestamp) == "Jan 1, 8:00");
    }

    SECTION("should handle timestamp at the end of the year") {
        long long timestamp = 1672531199;
        REQUIRE(timestampToReadableDate(timestamp) == "Jan 1, 7:59");
    }

    SECTION("should handle timestamps in the leap year") {
        long long timestamp = 1583020800;
        REQUIRE(timestampToReadableDate(timestamp) == "Mar 1, 8:00");
    }

    SECTION("should convert timestamp to readable format with single-digit day") {
        long long timestamp = 1675190400;
        REQUIRE(timestampToReadableDate(timestamp) == "Feb 1, 2:40");
    }

    SECTION("should handle zero UNIX timestamp") {
        long long timestamp = 0;
        REQUIRE(timestampToReadableDate(timestamp) == "Jan 1, 8:00");
    }
}