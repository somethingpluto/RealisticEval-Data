TEST_CASE("getCurrentDate", "[date]") {
    SECTION("should return a string in the format YYYY-MM-DD") {
        std::string date = getCurrentDate();
        REQUIRE(!date.empty());
        REQUIRE(std::regex_match(date, std::regex("^\\d{4}-\\d{2}-\\d{2}$")));
    }

    SECTION("should return the correct date for today") {
        std::string expectedDate = getCurrentDate(); // Get the current date using the function
        std::time_t now = std::time(0);
        std::tm* tm_now = std::localtime(&now);
        std::ostringstream oss;
        oss << std::put_time(tm_now, "%Y-%m-%d");
        std::string actualDate = oss.str();
        REQUIRE(actualDate == expectedDate);
    }

    SECTION("should return the correct year part in YYYY-MM-DD") {
        std::time_t now = std::time(0);
        std::tm* tm_now = std::localtime(&now);
        std::string currentYear = std::to_string(tm_now->tm_year + 1900);
        std::string actualDate = getCurrentDate();
        REQUIRE(actualDate.starts_with(currentYear));
    }

    SECTION("should return the correct month part in YYYY-MM-DD") {
        std::time_t now = std::time(0);
        std::tm* tm_now = std::localtime(&now);
        std::string currentMonth = std::to_string(tm_now->tm_mon + 1);
        if (currentMonth.length() < 2) {
            currentMonth = "0" + currentMonth; // Add leading zero if needed
        }
        std::string actualDate = getCurrentDate();
        REQUIRE(actualDate.substr(5, 2) == currentMonth);
    }

    SECTION("should return the correct day part in YYYY-MM-DD") {
        std::time_t now = std::time(0);
        std::tm* tm_now = std::localtime(&now);
        std::string currentDay = std::to_string(tm_now->tm_mday);
        if (currentDay.length() < 2) {
            currentDay = "0" + currentDay; // Add leading zero if needed
        }
        std::string actualDate = getCurrentDate();
        REQUIRE(actualDate.substr(8, 2) == currentDay);
    }
}