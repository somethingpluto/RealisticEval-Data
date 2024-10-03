TEST_CASE("printBoard outputs correct format", "[printBoard]") {
    vector<vector<char>> board1 = {
        {'X', 'O', 'X'},
        {' ', 'X', 'O'},
        {'O', ' ', ' '}
    };

    vector<vector<char>> board2 = {
        {' ', ' ', ' '},
        {' ', ' ', ' '},
        {' ', ' ', ' '}
    };

    vector<vector<char>> board3 = {
        {'X', 'X', 'X'},
        {'O', 'O', ' '},
        {' ', ' ', ' '}
    };

    vector<vector<char>> board4 = {
        {'O', 'O', 'O'},
        {'X', 'X', 'X'},
        {'X', 'O', ' '}
    };

    vector<vector<char>> board5 = {
        {'X', ' ', ' '},
        {' ', 'X', ' '},
        {' ', ' ', 'X'}
    };

    vector<vector<char>> board6 = {
        {' ', 'O', ' '},
        {'O', ' ', 'O'},
        {' ', 'O', ' '}
    };

    // Test case 1
    SECTION("Test case 1") {
        ostringstream output;
        streambuf* oldCoutBuffer = cout.rdbuf(output.rdbuf()); // Redirect cout to ostringstream

        printBoard(board1);

        cout.rdbuf(oldCoutBuffer); // Restore original cout
        string expectedOutput = "-------------\n| X | O | X | \n-------------\n|   | X | O | \n-------------\n| O |   |   | \n-------------\n";
        REQUIRE(output.str() == expectedOutput);
    }

    // Test case 2
    SECTION("Test case 2") {
        ostringstream output;
        streambuf* oldCoutBuffer = cout.rdbuf(output.rdbuf());

        printBoard(board2);

        cout.rdbuf(oldCoutBuffer);
        string expectedOutput = "-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n|   |   |   | \n-------------\n";
        REQUIRE(output.str() == expectedOutput);
    }

    // Test case 3
    SECTION("Test case 3") {
        ostringstream output;
        streambuf* oldCoutBuffer = cout.rdbuf(output.rdbuf());

        printBoard(board3);

        cout.rdbuf(oldCoutBuffer);
        string expectedOutput = "-------------\n| X | X | X | \n-------------\n| O | O |   | \n-------------\n|   |   |   | \n-------------\n";
        REQUIRE(output.str() == expectedOutput);
    }

    // Test case 4
    SECTION("Test case 4") {
        ostringstream output;
        streambuf* oldCoutBuffer = cout.rdbuf(output.rdbuf());

        printBoard(board4);

        cout.rdbuf(oldCoutBuffer);
        string expectedOutput = "-------------\n| O | O | O | \n-------------\n| X | X | X | \n-------------\n| X | O |   | \n-------------\n";
        REQUIRE(output.str() == expectedOutput);
    }

    // Test case 5
    SECTION("Test case 5") {
        ostringstream output;
        streambuf* oldCoutBuffer = cout.rdbuf(output.rdbuf());

        printBoard(board5);

        cout.rdbuf(oldCoutBuffer);
        string expectedOutput = "-------------\n| X |   |   | \n-------------\n|   | X |   | \n-------------\n|   |   | X | \n-------------\n";
        REQUIRE(output.str() == expectedOutput);
    }

    // Test case 6
    SECTION("Test case 6") {
        ostringstream output;
        streambuf* oldCoutBuffer = cout.rdbuf(output.rdbuf());

        printBoard(board6);

        cout.rdbuf(oldCoutBuffer);
        string expectedOutput = "-------------\n|   | O |   | \n-------------\n| O |   | O | \n-------------\n|   | O |   | \n-------------\n";
        REQUIRE(output.str() == expectedOutput);
    }
}