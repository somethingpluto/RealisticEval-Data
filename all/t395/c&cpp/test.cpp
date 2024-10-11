TEST_CASE("Sum Calibration Values", "[sum_calibration_values]") {
    SECTION("Single Line with Single Number") {
        std::vector<std::string> input = {"123"};
        REQUIRE(sum_calibration_values(input) == 13);
    }

    SECTION("Multiple Lines with Single Numbers") {
        std::vector<std::string> input = {"456", "789", "012"};
        REQUIRE(sum_calibration_values(input) == 12);
    }

    SECTION("Line with Multiple Numbers") {
        std::vector<std::string> input = {"12a34b56"};
        REQUIRE(sum_calibration_values(input) == 16);
    }

    SECTION("Empty Line") {
        std::vector<std::string> input = {""};
        REQUIRE(sum_calibration_values(input) == 0);
    }

    SECTION("No Numbers in Line") {
        std::vector<std::string> input = {"abc"};
        REQUIRE(sum_calibration_values(input) == 0);
    }
}