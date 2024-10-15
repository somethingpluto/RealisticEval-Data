TEST_CASE("formatBytes", "[formatBytes]") {
    SECTION("should return '0 Byte' for 0 bytes") {
        auto result = formatBytes(0);
        REQUIRE(result == "0 Byte" || result == "0 B");
    }

    SECTION("should return '2.0 KB' for 2048 bytes") {
        auto result = formatBytes(2048);
        REQUIRE(result == "2 KB" || result == "2.0 KB");
    }

    SECTION("should return '2.0 KiB' for 2048 bytes with sizeType 'accurate'") {
        auto result = formatBytes(2048, std::nullopt, "accurate");
        REQUIRE(result == "2 KiB" || result == "2.0 KiB");
    }

    SECTION("should return '5.0 MB' for 5242880 bytes") {
        auto result = formatBytes(5242880);
        REQUIRE(result == "5 MB" || result == "5.0 MB");
    }

    SECTION("should return '5.00 MiB' for 5242880 bytes with 2 decimal places and sizeType 'accurate'") {
        auto result = formatBytes(5242880, 2, "accurate");
        REQUIRE(result == "5.00 MiB");
    }
}