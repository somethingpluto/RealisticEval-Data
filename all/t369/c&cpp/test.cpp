TEST_CASE("Eight Queens Problem", "[eightQueens]") {
    // Call the function to solve the Eight Queens problem
    eightQueens();

    // Add assertions to check the expected behavior
    // For example, if the function prints the board, you can capture the output
    std::ostringstream oss;
    std::streambuf* oldCout = std::cout.rdbuf(oss.rdbuf());

    // Call the function again to capture the output
    eightQueens();

    std::string output = oss.str();
    std::cout.rdbuf(oldCout);

    // Check if the output contains the expected board configuration
    REQUIRE(output.find(". . Q . . . . .") != std::string::npos);
    REQUIRE(output.find(". . . . Q . . .") != std::string::npos);
    REQUIRE(output.find(". Q . . . . . .") != std::string::npos);
    REQUIRE(output.find(". . . . . . . Q") != std::string::npos);
    REQUIRE(output.find(". . . . . Q . .") != std::string::npos);
    REQUIRE(output.find(". . . Q . . . .") != std::string::npos);
    REQUIRE(output.find(". . . . . . Q .") != std::string::npos);
    REQUIRE(output.find("Q . . . . . . .") != std::string::npos);
}