TEST_CASE("sanitizeData removes specified keys", "[sanitizeData]") {
    // Test case 1: No keys to remove
    std::map<std::string, std::string> input1 = {{"name", "John"}, {"age", "30"}, {"city", "New York"}};
    std::vector<std::string> keysToRemove1 = {};
    std::map<std::string, std::string> expectedOutput1 = input1;
    REQUIRE(sanitizeData(input1, keysToRemove1) == expectedOutput1);

    // Test case 2: Single key to remove
    std::map<std::string, std::string> input2 = {{"name", "John"}, {"age", "30"}, {"city", "New York"}};
    std::vector<std::string> keysToRemove2 = {"age"};
    std::map<std::string, std::string> expectedOutput2 = {{"name", "John"}, {"city", "New York"}};
    REQUIRE(sanitizeData(input2, keysToRemove2) == expectedOutput2);

    // Test case 3: Multiple keys to remove
    std::map<std::string, std::string> input3 = {{"name", "John"}, {"age", "30"}, {"city", "New York"}, {"email", "john@example.com"}};
    std::vector<std::string> keysToRemove3 = {"age", "email"};
    std::map<std::string, std::string> expectedOutput3 = {{"name", "John"}, {"city", "New York"}};
    REQUIRE(sanitizeData(input3, keysToRemove3) == expectedOutput3);

    // Test case 4: Key not present in input
    std::map<std::string, std::string> input4 = {{"name", "John"}, {"age", "30"}, {"city", "New York"}};
    std::vector<std::string> keysToRemove4 = {"address"};
    std::map<std::string, std::string> expectedOutput4 = input4;
    REQUIRE(sanitizeData(input4, keysToRemove4) == expectedOutput4);
}