#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <vector>
#include <algorithm>
#include <string>
#include <set>

std::vector<int> shuffle(std::vector<int>& array); // Declaration of the shuffle function

TEST_CASE("shuffle function tests") {
    SECTION("shuffles an array of numbers") {
        std::vector<int> array = {1, 2, 3, 4, 5};
        std::vector<int> shuffledArray = array;
        shuffle(shuffledArray);

        REQUIRE(shuffledArray.size() == array.size());
        REQUIRE(std::all_of(shuffledArray.begin(), shuffledArray.end(), [&](int item) {
            return std::find(array.begin(), array.end(), item) != array.end();
        }));
        REQUIRE(std::set<int>(shuffledArray.begin(), shuffledArray.end()).size() ==
                std::set<int>(array.begin(), array.end()).size()); // Ensure no duplicates
    }

    SECTION("shuffles an array of strings") {
        std::vector<std::string> array = {"apple", "banana", "cherry", "date", "elderberry"};
        std::vector<std::string> shuffledArray = array;
        shuffle(shuffledArray);

        REQUIRE(shuffledArray.size() == array.size());
        REQUIRE(std::all_of(shuffledArray.begin(), shuffledArray.end(), [&](const std::string& item) {
            return std::find(array.begin(), array.end(), item) != array.end();
        }));
    }

    SECTION("shuffles an array with duplicate elements") {
        std::vector<int> array = {1, 1, 2, 2, 3, 3};
        std::vector<int> shuffledArray = array;
        shuffle(shuffledArray);

        REQUIRE(shuffledArray.size() == array.size());
        REQUIRE(std::all_of(shuffledArray.begin(), shuffledArray.end(), [&](int item) {
            return std::find(array.begin(), array.end(), item) != array.end();
        }));
    }

    SECTION("shuffles an array with a single element") {
        std::vector<int> array = {42};
        std::vector<int> shuffledArray = array;
        shuffle(shuffledArray);

        REQUIRE(shuffledArray == array);
    }

    SECTION("shuffles an empty array") {
        std::vector<int> array = {};
        std::vector<int> shuffledArray = array;
        shuffle(shuffledArray);

        REQUIRE(shuffledArray.size() == 0);
    }
}