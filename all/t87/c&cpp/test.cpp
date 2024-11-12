TEST_CASE("timestampToReadableDate", "[timestamp]") {
    SECTION("should convert UNIX timestamp to readable format") {
        long long timestamp = 1696516800;
        REQUIRE(timestamp_to_readable_date(timestamp) == "Oct 05, 10:40 PM");
    }

    SECTION("should handle timestamp at the start of the year") {
        long long timestamp = 1672531200;
        REQUIRE(timestamp_to_readable_date(timestamp) == "Jan 01, 8:00 AM");
    }

    SECTION("should handle timestamp at the end of the year") {
        long long timestamp = 1672531199;
        REQUIRE(timestamp_to_readable_date(timestamp) == "Jan 01, 7:59 AM");
    }

    SECTION("should handle timestamps in the leap year") {
        long long timestamp = 1583020800;
        REQUIRE(timestamp_to_readable_date(timestamp) == "Mar 01, 8:00 AM");
    }

    SECTION("should convert timestamp to readable format with single-digit day") {
        long long timestamp = 1675190400;
        REQUIRE(timestamp_to_readable_date(timestamp) == "Feb 01, 2:40 AM");
    }

    SECTION("should handle zero UNIX timestamp") {
        long long timestamp = 0;
        REQUIRE(timestamp_to_readable_date(timestamp) == "Jan 01, 8:00 AM");
    }
}