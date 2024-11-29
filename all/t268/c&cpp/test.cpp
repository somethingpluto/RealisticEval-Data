TEST_CASE("Test possible single station", "[canCompleteCircuit]") {
    std::vector<int> gas = {5};
    std::vector<int> cost = {4};
    int expected = 0;
    REQUIRE(can_complete_circuit(gas, cost) == expected);
}

TEST_CASE("Test impossible single station", "[canCompleteCircuit]") {
    std::vector<int> gas = {4};
    std::vector<int> cost = {5};
    int expected = -1;
    REQUIRE(can_complete_circuit(gas, cost) == expected);
}

TEST_CASE("Test two stations possible", "[canCompleteCircuit]") {
    std::vector<int> gas = {1, 2};
    std::vector<int> cost = {2, 1};
    int expected = 1;
    REQUIRE(can_complete_circuit(gas, cost) == expected);
}

TEST_CASE("Test circular route possible", "[canCompleteCircuit]") {
    std::vector<int> gas = {1, 2, 3, 4, 5};
    std::vector<int> cost = {3, 4, 5, 1, 2};
    int expected = 3;
    REQUIRE(can_complete_circuit(gas, cost) == expected);
}

TEST_CASE("Test circular route impossible", "[canCompleteCircuit]") {
    std::vector<int> gas = {2, 3, 4};
    std::vector<int> cost = {3, 4, 3};
    int expected = -1;
    REQUIRE(can_complete_circuit(gas, cost) == expected);
}