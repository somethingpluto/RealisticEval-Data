TEST_CASE("Get Current Date Info") {
    auto now = std::localtime(nullptr);
    DateInfo result = get_current_date_info(*now);

    REQUIRE(result.year == now->tm_year + 1900); // Year since 1900
    REQUIRE(result.month == { "January", "February", "March", "April", "May", "June",
                              "July", "August", "September", "October", "November", "December" }[now->tm_mon]);
    REQUIRE(result.weekOfTheMonth == ((now->tm_mday - 1) / 7) + 1);
    REQUIRE(result.dayOfWeek == { "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" }[now->tm_wday]);
}