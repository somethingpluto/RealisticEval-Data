TEST_CASE("General case", "[findMaxDifference]") {
    vector<int> l = {2, 3, 10, 6, 4, 8, 1};
    REQUIRE(findMaxDifference(l) == 8);  // 最大差值是 10 - 2 = 8
}

// 测试用例 2: 递减序列
TEST_CASE("Decreasing sequence", "[findMaxDifference]") {
    vector<int> l = {10, 9, 8, 7, 6, 5};
    REQUIRE(findMaxDifference(l) == -1);  // 最大差值是 9 - 10 = -1
}

// 测试用例 3: 全部相同元素
TEST_CASE("All elements the same", "[findMaxDifference]") {
    vector<int> l = {5, 5, 5, 5, 5};
    REQUIRE(findMaxDifference(l) == 0);  // 最大差值是 5 - 5 = 0
}

// 测试用例 4: 只有两个元素
TEST_CASE("Only two elements", "[findMaxDifference]") {
    vector<int> l = {3, 8};
    REQUIRE(findMaxDifference(l) == 5);  // 最大差值是 8 - 3 = 5
}

// 测试用例 5: 只有一个元素
TEST_CASE("Single element", "[findMaxDifference]") {
    vector<int> l = {4};
    REQUIRE(findMaxDifference(l) == numeric_limits<int>::min());  // 只有一个元素，无法计算差值
}