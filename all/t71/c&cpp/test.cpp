TEST_CASE("Test read_columns function", "[read_columns]") {
    const std::string test_file = "test_file.txt";

    SECTION("Basic functionality") {
        // Test reading a file with a valid structure and numerical question
        std::string content = R"(
Line 1
Line 2
/
1.0 2.0 3.0
4.0 5.0 6.0
)";
        std::ofstream file(test_file);
        file << content;
        file.close();

        std::vector<std::vector<double>> result = read_columns(test_file);
        std::vector<std::vector<double>> expected_result = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        REQUIRE(result == expected_result);

        if (std::remove(test_file.c_str()) != 0) {
            std::cerr << "Failed to remove test file." << std::endl;
        }
    }

    SECTION("No slash character") {
        // Test that a runtime_error is raised if no '/' character is found
        std::string content = R"(
Line 1
Line 2
Line 3
)";
        std::ofstream file(test_file);
        file << content;
        file.close();

        REQUIRE_THROWS_AS(read_columns(test_file), std::runtime_error);

        if (std::remove(test_file.c_str()) != 0) {
            std::cerr << "Failed to remove test file." << std::endl;
        }
    }

    SECTION("File with comments and empty lines") {
        // Test handling of comments and empty lines
        std::string content = R"(
Line 1
/
! This is a comment
1.0 2.0 3.0

4.0 5.0 6.0
! Another comment
)";
        std::ofstream file(test_file);
        file << content;
        file.close();

        std::vector<std::vector<double>> result = read_columns(test_file);
        std::vector<std::vector<double>> expected_result = {{1.0, 2.0, 3.0}, {4.0, 5.0, 6.0}};
        REQUIRE(result == expected_result);

        if (std::remove(test_file.c_str()) != 0) {
            std::cerr << "Failed to remove test file." << std::endl;
        }
    }

    SECTION("Different number of columns") {
        // Test that the function handles different number of columns correctly
        std::string content = R"(
Line 1
/
1.0 2.0
3.0 4.0
5.0 6.0 7.0
)";
        std::ofstream file(test_file);
        file << content;
        file.close();

        REQUIRE_THROWS_AS(read_columns(test_file), std::runtime_error);

        if (std::remove(test_file.c_str()) != 0) {
            std::cerr << "Failed to remove test file." << std::endl;
        }
    }

    SECTION("Empty file") {
        // Test handling of an empty file
        std::string content = "";
        std::ofstream file(test_file);
        file << content;
        file.close();

        REQUIRE_THROWS_AS(read_columns(test_file), std::runtime_error);

        if (std::remove(test_file.c_str()) != 0) {
            std::cerr << "Failed to remove test file." << std::endl;
        }
    }
}