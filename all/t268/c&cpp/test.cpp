TEST_CASE("Test canCompleteCircuit", "[canCompleteCircuit]") {
    REQUIRE(canCompleteCircuit({1, 2, 3, 4, 5}, {3, 4, 5, 1, 2}) == 3);
    REQUIRE(canCompleteCircuit({2, 3, 4}, {3, 4, 3}) == -1);
}