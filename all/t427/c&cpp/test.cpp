TEST_CASE("TestCheckSequences", "[check_sequences]") {
    // Set up the test cases with sequences.
    std::string test_file = "test_sequences.dat";

    // Write test sequences to the file
    std::ofstream f(test_file);
    f << "2,4,6,8\n";    // Munodi sequence (d = 2)
    f << "1,3,5,7\n";    // Munodi sequence (d = 2)
    f << "10,20,30\n";   // Munodi sequence (d = 10)
    f << "1,2,4,8\n";    // Not a Munodi sequence (d changes)
    f << "5,10,15,20\n"; // Munodi sequence (d = 5)
    f.close();

    // Expected results
    std::map<std::vector<int>, bool> expected_results = {
        {{2, 4, 6, 8}, true},
        {{1, 3, 5, 7}, true},
        {{10, 20, 30}, true},
        {{1, 2, 4, 8}, false},
        {{5, 10, 15, 20}, true}
    };

    // Check the sequences
    auto results = check_sequences(test_file);
    for (const auto& [seq, expected] : expected_results) {
        REQUIRE(results.find(seq) != results.end());
        CHECK(results.at(seq) == expected);
    }

    // Clean up the test file after tests
    std::filesystem::remove(test_file);
}