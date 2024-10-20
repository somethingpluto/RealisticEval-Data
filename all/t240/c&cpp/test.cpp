TEST_CASE("TestGenTimeoutTimedelta", "[gen_timeout_duration]") {
    SECTION("test_single_unit_days") {
        REQUIRE(gen_timeout_duration("5d") == std::chrono::days(5));
    }

    SECTION("test_single_unit_hours") {
        REQUIRE(gen_timeout_duration("8h") == std::chrono::hours(8));
    }

    SECTION("test_single_unit_minutes") {
        REQUIRE(gen_timeout_duration("45m") == std::chrono::minutes(45));
    }

    SECTION("test_single_unit_seconds") {
        REQUIRE(gen_timeout_duration("30s") == std::chrono::seconds(30));
    }

    SECTION("test_complex_mix") {
        REQUIRE(gen_timeout_duration("2d 20h 30m") == (std::chrono::days(2) + std::chrono::hours(20) + std::chrono::minutes(30)));
    }

    SECTION("test_no_units") {
        REQUIRE(gen_timeout_duration("") == std::chrono::milliseconds(0));
    }
}