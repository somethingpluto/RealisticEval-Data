TEST_CASE("Testing minChangesToSymmetric function") {

    SECTION("Already Symmetric Matrix") {
        vector<vector<char>> matrix = {
            {'a', 'b', 'c'},
            {'b', 'e', 'f'},
            {'c', 'f', 'i'}
        };
        REQUIRE(minChangesToSymmetric(matrix) == 0);
    }

    SECTION("One Change Needed") {
        vector<vector<char>> matrix = {
            {'a', 'b', 'c'},
            {'d', 'e', 'f'},
            {'c', 'h', 'i'}
        };
        REQUIRE(minChangesToSymmetric(matrix) == 2);
    }

    SECTION("All Different Elements") {
        vector<vector<char>> matrix = {
            {'a', 'b', 'c'},
            {'d', 'e', 'f'},
            {'g', 'h', 'i'}
        };
        REQUIRE(minChangesToSymmetric(matrix) == 3);
    }

    SECTION("Large Symmetric Matrix") {
        vector<vector<char>> matrix = {
            {'a', 'b', 'c', 'd'},
            {'b', 'e', 'f', 'g'},
            {'c', 'f', 'h', 'i'},
            {'d', 'g', 'i', 'j'}
        };
        REQUIRE(minChangesToSymmetric(matrix) == 0);
    }

    SECTION("Multiple Changes Needed") {
        vector<vector<char>> matrix = {
            {'a', 'x', 'c', 'd'},
            {'y', 'e', 'f', 'g'},
            {'z', 'h', 'i', 'j'},
            {'d', 'g', 'k', 'l'}
        };
        REQUIRE(minChangesToSymmetric(matrix) == 4);
    }
}
