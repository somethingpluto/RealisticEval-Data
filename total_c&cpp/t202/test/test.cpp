TEST_CASE("Leap year February", "[getDaysInMonth]") {
    REQUIRE(getDaysInMonth(2024, 2) == 29); // 2024 是闰年
}

// 测试用例 2: 非闰年的二月份
TEST_CASE("Non-leap year February", "[getDaysInMonth]") {
    REQUIRE(getDaysInMonth(2023, 2) == 28); // 2023 不是闰年
}

// 测试用例 3: 大月份（31天）的情况
TEST_CASE("Month with 31 days", "[getDaysInMonth]") {
    REQUIRE(getDaysInMonth(2023, 1) == 31); // 一月份有 31 天
    REQUIRE(getDaysInMonth(2023, 7) == 31); // 七月份有 31 天
}

// 测试用例 4: 小月份（30天）的情况
TEST_CASE("Month with 30 days", "[getDaysInMonth]") {
    REQUIRE(getDaysInMonth(2023, 4) == 30); // 四月份有 30 天
    REQUIRE(getDaysInMonth(2023, 11) == 30); // 十一月份有 30 天
}

// 测试用例 5: 无效的月份
TEST_CASE("Invalid month", "[getDaysInMonth]") {
    REQUIRE_THROWS_AS(getDaysInMonth(2023, 0), std::invalid_argument);  // 月份小于 1
    REQUIRE_THROWS_AS(getDaysInMonth(2023, 13), std::invalid_argument); // 月份大于 12
}