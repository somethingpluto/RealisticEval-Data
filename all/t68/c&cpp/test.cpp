TEST_CASE("Divide list into equal parts", "[divide_list]") {
    SECTION("List with 5 elements divided into 3 parts") {
        std::vector<int> input = {1, 2, 3, 4, 5};
        auto result = divide_list(input, 3);
        REQUIRE(result.size() == 3);
        REQUIRE(result[0] == std::vector<int>({1, 2}));
        REQUIRE(result[1] == std::vector<int>({3, 4}));
        REQUIRE(result[2] == std::vector<int>({5}));
    }

    SECTION("List with 6 elements divided into 3 parts") {
        std::vector<int> input = {1, 2, 3, 4, 5, 6};
        auto result = divide_list(input, 3);
        REQUIRE(result.size() == 3);
        REQUIRE(result[0] == std::vector<int>({1, 2}));
        REQUIRE(result[1] == std::vector<int>({3, 4}));
        REQUIRE(result[2] == std::vector<int>({5, 6}));
    }

    SECTION("List with 7 elements divided into 3 parts") {
        std::vector<int> input = {1, 2, 3, 4, 5, 6, 7};
        auto result = divide_list(input, 3);
        REQUIRE(result.size() == 3);
        REQUIRE(result[0] == std::vector<int>({1, 2}));
        REQUIRE(result[1] == std::vector<int>({3, 4}));
        REQUIRE(result[2] == std::vector<int>({5, 6, 7}));
    }

    SECTION("List with 0 elements divided into 3 parts") {
        std::vector<int> input = {};
        auto result = divide_list(input, 3);
        REQUIRE(result.size() == 0);
    }

    SECTION("List with 5 elements divided into 1 part") {
        std::vector<int> input = {1, 2, 3, 4, 5};
        auto result = divide_list(input, 1);
        REQUIRE(result.size() == 1);
        REQUIRE(result[0] == std::vector<int>({1, 2, 3, 4, 5}));
    }

    SECTION("List with 5 elements divided into 0 parts should throw exception") {
        std::vector<int> input = {1, 2, 3, 4, 5};
        CHECK_THROWS_AS(divide_list(input, 0), std::invalid_argument);
    }
}