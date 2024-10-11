TEST_CASE("Test get_min_seq_num_and_distance", "[file_processing]") {
    // Test case 1: Words found in different lines
    SECTION("Words in different lines") {
        auto result = get_min_seq_num_and_distance("test_data.txt", "word1", "word2");
        REQUIRE(std::get<0>(result) == 2);  // Assuming the minimum distance is on line 2
        REQUIRE(std::get<1>(result) == 3);  // Assuming the minimum distance is 3
    }

    // Test case 2: Words found in the same line
    SECTION("Words in the same line") {
        auto result = get_min_seq_num_and_distance("test_data.txt", "word1", "word2");
        REQUIRE(std::get<0>(result) == 1);  // Assuming the minimum distance is on line 1
        REQUIRE(std::get<1>(result) == 1);  // Assuming the minimum distance is 1
    }

    // Test case 3: One word not found
    SECTION("One word not found") {
        auto result = get_min_seq_num_and_distance("test_data.txt", "word1", "nonexistent_word");
        REQUIRE(std::get<0>(result) == -1);  // Assuming -1 indicates not found
        REQUIRE(std::get<1>(result) == std::numeric_limits<int>::max());  // Assuming max int indicates not found
    }

    // Test case 4: Both words not found
    SECTION("Both words not found") {
        auto result = get_min_seq_num_and_distance("test_data.txt", "nonexistent_word1", "nonexistent_word2");
        REQUIRE(std::get<0>(result) == -1);  // Assuming -1 indicates not found
        REQUIRE(std::get<1>(result) == std::numeric_limits<int>::max());  // Assuming max int indicates not found
    }
}