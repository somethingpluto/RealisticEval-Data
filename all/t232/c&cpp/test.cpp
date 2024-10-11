TEST_CASE("convert_hms_to_milliseconds tests") {
    
    SECTION("Basic conversion") {
        REQUIRE(convert_hms_to_milliseconds("1h20min30s") == 4830000);
    }

    SECTION("No hours or minutes") {
        REQUIRE(convert_hms_to_milliseconds("30s") == 30000);
    }

    SECTION("Invalid format") {
        REQUIRE(convert_hms_to_milliseconds("1hour20minutes") == std::nullopt);
    }

    SECTION("Edge case max one day") {
        REQUIRE(convert_hms_to_milliseconds("23h59min59s") == 86399000);
    }

    SECTION("Exceeding one day") {
        REQUIRE(convert_hms_to_milliseconds("24h1min") == 86460000);
    }
}
