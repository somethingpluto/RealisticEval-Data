TEST_CASE("Test Eight Queens Problem") {
    SECTION("Test Solution Exists") {
        std::ostringstream out;
        {
            std::streambuf* prevcoutbuf = std::cout.rdbuf(out.rdbuf());
            eightQueens();
            std::cout.rdbuf(prevcoutbuf);
        }

        REQUIRE(out.str().find("Q") != std::string::npos);
    }

    SECTION("Test Correct Number of Queens") {
        std::ostringstream out;
        {
            std::streambuf* prevcoutbuf = std::cout.rdbuf(out.rdbuf());
            eightQueens();
            std::cout.rdbuf(prevcoutbuf);
        }

        std::istringstream iss(out.str());
        std::string line;
        while (std::getline(iss, line)) {
            int numQueens = std::count(line.begin(), line.end(), 'Q');
            REQUIRE(numQueens == 8);
        }
    }

    SECTION("Test No Solution Scenario") {
        std::ostringstream out;
        {
            std::streambuf* prevcoutbuf = std::cout.rdbuf(out.rdbuf());
            noSolutionQueens();
            std::cout.rdbuf(prevcoutbuf);
        }

        REQUIRE(out.str().find("No solution") != std::string::npos);
    }
}