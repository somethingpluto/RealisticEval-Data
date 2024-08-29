TEST_CASE("Days in month calculation", "[days_in_month]") {
SECTION("February in a Common Year") {
REQUIRE(days_in_month(2021, 2)
== 28);
}
SECTION("February in a Leap Year") {
REQUIRE(days_in_month(2020, 2)
== 29);
}
SECTION("April") {
REQUIRE(days_in_month(2021, 4)
== 30);
}
SECTION("December") {
REQUIRE(days_in_month(2021, 12)
== 31);
}
SECTION("January in a Leap Year") {
REQUIRE(days_in_month(2020, 1)
== 31);
}
}