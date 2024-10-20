
TEST_CASE("Testwrite_unique_line_to_file", "[write_unique_line_to_file]") {

    const std::string filename = "test_file.txt";

    SECTION("Setup: Create a temporary file for testing") {
        std::ofstream file(filename);
        REQUIRE(file.is_open());
        file.close();
    }

    SECTION("Test case 1: Writing a new line to an empty file") {
        const std::string lineContent = "First unique line.";

        write_unique_line_to_file(filename, lineContent);


        std::ifstream file(filename);
        REQUIRE(file.is_open());

        std::string fileContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        REQUIRE(fileContent.find(lineContent) != std::string::npos);
    }

    SECTION("Test case 2: Attempting to write a duplicate line") {
        const std::string lineContent = "First unique line.";

        write_unique_line_to_file(filename, lineContent);
        write_unique_line_to_file(filename, lineContent);


        std::ifstream file(filename);
        REQUIRE(file.is_open());

        std::string fileContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        REQUIRE(std::count(fileContent.begin(), fileContent.end(), '\n') == 1);
        REQUIRE(fileContent.find(lineContent) != std::string::npos);
    }

    SECTION("Test case 3: Writing multiple unique lines") {
        const std::vector<std::string> lines = {"First unique line.", "Second unique line.", "Third unique line."};
        for (const auto& line : lines) {

            write_unique_line_to_file(filename, line);

        }

        std::ifstream file(filename);
        REQUIRE(file.is_open());

        std::string fileContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        for (const auto& line : lines) {
            REQUIRE(fileContent.find(line) != std::string::npos);
        }
    }

    SECTION("Test case 4: Writing an empty line, should not write") {
        const std::string lineContent = "";

        write_unique_line_to_file(filename, lineContent);


        std::ifstream file(filename);
        REQUIRE(file.is_open());

        std::string fileContent((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());
        REQUIRE(fileContent.empty());
    }

}