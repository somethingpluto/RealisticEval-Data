TEST_CASE("getCurrentDate function") {

    SECTION("Correct format YYYY-MM-DD") {
        std::string currentDate = getCurrentDate();
        REQUIRE(currentDate.length() == 10);
        REQUIRE(currentDate[4] == '-');
        REQUIRE(currentDate[7] == '-');
    }

    SECTION("Returns correct year") {
        std::time_t t = std::time(nullptr);
        std::tm* now = std::localtime(&t);
        int currentYear = now->tm_year + 1900;

        std::string currentDate = getCurrentDate();
        std::string yearPart = currentDate.substr(0, 4);

        REQUIRE(std::stoi(yearPart) == currentYear);
    }

    SECTION("Returns correct month") {
        std::time_t t = std::time(nullptr);
        std::tm* now = std::localtime(&t);
        int currentMonth = now->tm_mon + 1;

        std::string currentDate = getCurrentDate();
        std::string monthPart = currentDate.substr(5, 2);

        REQUIRE(std::stoi(monthPart) == currentMonth);
    }

    SECTION("Returns correct day") {
        std::time_t t = std::time(nullptr);
        std::tm* now = std::localtime(&t);
        int currentDay = now->tm_mday;

        std::string currentDate = getCurrentDate();
        std::string dayPart = currentDate.substr(8, 2);

        REQUIRE(std::stoi(dayPart) == currentDay);
    }

    SECTION("Consistency of output within the same second") {
        std::string firstCall = getCurrentDate();
        std::string secondCall = getCurrentDate();
        REQUIRE(firstCall == secondCall);
    }
}
