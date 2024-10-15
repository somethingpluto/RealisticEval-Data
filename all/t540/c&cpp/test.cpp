TEST_CASE("generateUniquePairs") {
    SECTION("generates unique pairs from an array with three elements") {
        vector<variant<int, string, struct {string key;}>> items = {"A", "B", "C"};
        auto result = generateUniquePairs(items);
        REQUIRE(result == vector<vector<variant<int, string, struct {string key;}>>>{ 
            {"A", "B"},
            {"A", "C"},
            {"B", "C"}
        });
    }

    SECTION("generates unique pairs from an array with two elements") {
        vector<variant<int, string, struct {string key;}>> items = {"A", "B"};
        auto result = generateUniquePairs(items);
        REQUIRE(result == vector<vector<variant<int, string, struct {string key;}>>>{ 
            {"A", "B"}
        });
    }

    SECTION("returns an empty array when the input array is empty") {
        vector<variant<int, string, struct {string key;}>> items = {};
        auto result = generateUniquePairs(items);
        REQUIRE(result.empty());
    }

    SECTION("returns an empty array when the input array has one element") {
        vector<variant<int, string, struct {string key;}>> items = {"A"};
        auto result = generateUniquePairs(items);
        REQUIRE(result.empty());
    }

    SECTION("handles an array with different types of elements") {
        vector<variant<int, string, struct {string key;}>> items = {1, "A", { "value" }};
        auto result = generateUniquePairs(items);
        REQUIRE(result == vector<vector<variant<int, string, struct {string key;}>>>{ 
            {1, "A"},
            {1, { "value" }},
            {"A", { "value" }}
        });
    }

    SECTION("generates pairs from an array with more than three elements") {
        vector<variant<int, string, struct {string key;}>> items = {"A", "B", "C", "D"};
        auto result = generateUniquePairs(items);
        REQUIRE(result == vector<vector<variant<int, string, struct {string key;}>>>{ 
            {"A", "B"},
            {"A", "C"},
            {"A", "D"},
            {"B", "C"},
            {"B", "D"},
            {"C", "D"}
        });
    }
}