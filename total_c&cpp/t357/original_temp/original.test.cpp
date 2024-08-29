#define CATCH_CONFIG_MAIN
#include "../../lib/catch.hpp"
#include "../original.cpp"
TEST_CASE("ShellSort Test Cases", "[shell_sort]") {
    // Test Case 1: Sorting an already sorted array
    vector<int> arr1 = {1, 2, 3, 4, 5};
    Sort_stats stats1 = shell_sort(arr1);
    REQUIRE(arr1 == vector<int>{1, 2, 3, 4, 5});
    REQUIRE(stats1.algorithm_name == "Shell sort");
    REQUIRE(stats1.array_size == 5);
    REQUIRE(stats1.comparisons > 0);
    REQUIRE(stats1.run_time >= 0);

    // Test Case 2: Sorting a reverse sorted array
    vector<int> arr2 = {5, 4, 3, 2, 1};
    Sort_stats stats2 = shell_sort(arr2);
    REQUIRE(arr2 == vector<int>{1, 2, 3, 4, 5});
    REQUIRE(stats2.algorithm_name == "Shell sort");
    REQUIRE(stats2.array_size == 5);
    REQUIRE(stats2.comparisons > 0);
    REQUIRE(stats2.run_time >= 0);

    // Test Case 3: Sorting an array with duplicate elements
    vector<int> arr3 = {3, 1, 2, 3, 2};
    Sort_stats stats3 = shell_sort(arr3);
    REQUIRE(arr3 == vector<int>{1, 2, 2, 3, 3});
    REQUIRE(stats3.algorithm_name == "Shell sort");
    REQUIRE(stats3.array_size == 5);
    REQUIRE(stats3.comparisons > 0);
    REQUIRE(stats3.run_time >= 0);

    // Test Case 4: Sorting an array with a single element
    vector<int> arr4 = {1};
    Sort_stats stats4 = shell_sort(arr4);
    REQUIRE(arr4 == vector<int>{1});
    REQUIRE(stats4.algorithm_name == "Shell sort");
    REQUIRE(stats4.array_size == 1);
    REQUIRE(stats4.comparisons == 0);  // No comparisons should be needed
    REQUIRE(stats4.run_time >= 0);

    // Test Case 5: Sorting an empty array
    vector<int> arr5 = {};
    Sort_stats stats5 = shell_sort(arr5);
    REQUIRE(arr5 == vector<int>{});
    REQUIRE(stats5.algorithm_name == "Shell sort");
    REQUIRE(stats5.array_size == 0);
    REQUIRE(stats5.comparisons == 0);  // No comparisons should be needed
    REQUIRE(stats5.run_time >= 0);
}