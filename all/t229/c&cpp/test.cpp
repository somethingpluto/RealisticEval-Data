TEST_CASE("TestFileSizeConverter", "[FileSizeConverter]") {
    SECTION("test_zero_bytes") {
        REQUIRE(convert_file_size(0) == "0B");
    }

    SECTION("test_bytes_less_than_1KB") {
        REQUIRE(convert_file_size(512) == "512B");
    }

    SECTION("test_exactly_1KB") {
        REQUIRE(convert_file_size(1024) == "1KB");
    }

    SECTION("test_2KB") {
        REQUIRE(convert_file_size(2048) == "2KB");
    }

    SECTION("test_exactly_1MB") {
        REQUIRE(convert_file_size(1048576) == "1MB");
    }

    SECTION("test_5MB") {
        REQUIRE(convert_file_size(5242880) == "5MB");
    }

    SECTION("test_exactly_1GB") {
        REQUIRE(convert_file_size(1073741824) == "1GB");
    }
}