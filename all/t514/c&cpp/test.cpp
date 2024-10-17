#include <catch2/catch_test_macros.hpp>
#include <regex>
#include <string>

TEST_CASE("TestExtractDateFromFilename", "[extract_date_from_filename]") {
    SECTION("test_date_extraction_success") {
        // Test case where the date is successfully extracted.
        const std::string file_name = "report-2023-09-28.txt";
        const std::string expected_date = "2023-09-28";
        REQUIRE(extract_date_from_filename(file_name) == expected_date);
    }

    SECTION("test_no_date_in_filename") {
        // Test case where no date is present in the filename.
        const std::string file_name = "report.txt";
        REQUIRE(extract_date_from_filename(file_name).empty());
    }

    SECTION("test_multiple_dates_in_filename") {
        // Test case where multiple dates are present, should return the first one.
        const std::string file_name = "report-2023-09-28-backup-2023-10-01.txt";
        const std::string expected_date = "2023-09-28";
        REQUIRE(extract_date_from_filename(file_name) == expected_date);
    }

    SECTION("test_date_at_start_of_filename") {
        // Test case where the date is at the start of the filename.
        const std::string file_name = "2023-09-28-report.txt";
        const std::string expected_date = "2023-09-28";
        REQUIRE(extract_date_from_filename(file_name) == expected_date);
    }

    SECTION("test_incorrect_date_format") {
        // Test case where the date format is incorrect.
        const std::string file_name = "report-2023-99-99.txt";  // Invalid date
        const std::string expected_date = "";  // Since the regex does not match, it should return an empty string
        REQUIRE(extract_date_from_filename(file_name).empty());
    }
}