TEST_CASE("TestPrependToEachLine") {
    std::string test_file_path = "test_file.txt";

    SECTION("setUp") {
        // Create a temporary file for testing
        std::ofstream f(test_file_path);
        f << "Line 1\nLine 2\nLine 3";
        f.close();
    }

    SECTION("tearDown") {
        // Remove the temporary file after testing
        std::filesystem::remove(test_file_path);
    }

    SECTION("test_prepend_string") {
        // Test appending a simple string to the beginning of each line
        prepend_to_each_line(test_file_path, "Test: ");
        std::ifstream f(test_file_path);
        std::string line;
        std::vector<std::string> lines;
        while (std::getline(f, line)) {
            lines.push_back(line + "\n");
        }
        f.close();
        REQUIRE(lines == std::vector<std::string>({
            "Test: Line 1\n",
            "Test: Line 2\n",
            "Test: Line 3\n"
        }));
    }

    SECTION("test_prepend_empty_string") {
        // Test appending an empty string
        prepend_to_each_line(test_file_path, "");
        std::ifstream f(test_file_path);
        std::string line;
        std::vector<std::string> lines;
        while (std::getline(f, line)) {
            lines.push_back(line + "\n");
        }
        f.close();
        REQUIRE(lines == std::vector<std::string>({
            "Line 1\n",
            "Line 2\n",
            "Line 3\n"
        }));
    }

    SECTION("test_prepend_special_characters") {
        // Test appending special characters to the beginning of each line
        prepend_to_each_line(test_file_path, "#$%^&* ");
        std::ifstream f(test_file_path);
        std::string line;
        std::vector<std::string> lines;
        while (std::getline(f, line)) {
            lines.push_back(line + "\n");
        }
        f.close();
        REQUIRE(lines == std::vector<std::string>({
            "#$%^&* Line 1\n",
            "#$%^&* Line 2\n",
            "#$%^&* Line 3\n"
        }));
    }

    SECTION("test_prepend_numeric_string") {
        // Test appending numeric string to the beginning of each line
        prepend_to_each_line(test_file_path, "123 ");
        std::ifstream f(test_file_path);
        std::string line;
        std::vector<std::string> lines;
        while (std::getline(f, line)) {
            lines.push_back(line + "\n");
        }
        f.close();
        REQUIRE(lines == std::vector<std::string>({
            "123 Line 1\n",
            "123 Line 2\n",
            "123 Line 3\n"
        }));
    }

    SECTION("test_file_not_found") {
        // Test the response when the file does not exist
        REQUIRE_THROWS_AS(prepend_to_each_line("non_existent_file.txt", "Test: "), std::runtime_error);
    }
}