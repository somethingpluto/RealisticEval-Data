TEST_CASE("Test read_mapping_file function", "[read_mapping_file]") {
    SECTION("Test with a valid mapping file content") {
        // Test with a valid mapping file content
        const std::string mock_file_content = "'old_pattern1','new_word1'\n'old_pattern2','new_word2'\n";
        std::istringstream mock_stream(mock_file_content);

        // Redirect std::ifstream to use the mock stream
        std::istringstream* original_ifstream_open = std::ifstream::open;
        std::ifstream::open = [&mock_stream](const std::string&, std::ios_base::openmode) {
            return &mock_stream;
        };

        std::vector<Mapping> result = read_mapping_file("dummy_path.txt");
        std::vector<Mapping> expected = {
            {std::regex("old_pattern1"), "new_word1"},
            {std::regex("old_pattern2"), "new_word2"}
        };

        REQUIRE(result.size() == expected.size());
        for (size_t i = 0; i < result.size(); ++i) {
            REQUIRE(result[i].pattern.mark_count() == expected[i].pattern.mark_count());
            REQUIRE(result[i].replacement == expected[i].replacement);
        }

        // Restore the original ifstream::open
        std::ifstream::open = original_ifstream_open;
    }

    SECTION("Test with a missing file") {
        // Test with a missing file
        REQUIRE_THROWS_AS(read_mapping_file("non_existent_file.txt"), std::runtime_error);
    }

    SECTION("Test with a line that does not contain a comma") {
        // Test with a line that does not contain a comma
        const std::string mock_file_content = "'old_pattern1' 'new_word1'\n";
        std::istringstream mock_stream(mock_file_content);

        // Redirect std::ifstream to use the mock stream
        std::istringstream* original_ifstream_open = std::ifstream::open;
        std::ifstream::open = [&mock_stream](const std::string&, std::ios_base::openmode) {
            return &mock_stream;
        };

        REQUIRE_THROWS_AS(read_mapping_file("dummy_path.txt"), std::runtime_error);

        // Restore the original ifstream::open
        std::ifstream::open = original_ifstream_open;
    }

    SECTION("Test with valid patterns that contain special regex characters") {
        // Test with valid patterns that contain special regex characters
        const std::string mock_file_content = "'\\d+', 'number'\n'\\w+', 'word'\n";
        std::istringstream mock_stream(mock_file_content);

        // Redirect std::ifstream to use the mock stream
        std::istringstream* original_ifstream_open = std::ifstream::open;
        std::ifstream::open = [&mock_stream](const std::string&, std::ios_base::openmode) {
            return &mock_stream;
        };

        std::vector<Mapping> result = read_mapping_file("dummy_path.txt");
        std::vector<Mapping> expected = {
            {std::regex("\\d+"), "number"},
            {std::regex("\\w+"), "word"}
        };

        REQUIRE(result.size() == expected.size());
        for (size_t i = 0; i < result.size(); ++i) {
            REQUIRE(result[i].pattern.mark_count() == expected[i].pattern.mark_count());
            REQUIRE(result[i].replacement == expected[i].replacement);
        }

        // Restore the original ifstream::open
        std::ifstream::open = original_ifstream_open;
    }
}
