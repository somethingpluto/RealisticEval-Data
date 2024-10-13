TEST_CASE("Test rename_file_path function", "[rename_file_path]") {
    SECTION("Test path with colon in the filename") {
        // Test path with colon in the filename
        std::string path = "C:\\Users\\example\\Documents\\report:2023.txt";
        std::string expected = "C:\\Users\\example\\Documents\\report_2023.txt";
        REQUIRE(rename_file_path(path) == expected);
    }

    SECTION("Test path without colon in the filename") {
        // Test path without colon in the filename
        std::string path = "C:\\Users\\example\\Documents\\report2023.txt";
        std::string expected = "C:\\Users\\example\\Documents\\report2023.txt";
        REQUIRE(rename_file_path(path) == expected);
    }

    SECTION("Test path with multiple colons in the filename") {
        // Test path with multiple colons in the filename
        std::string path = "C:\\Users\\example\\Documents\\project:report:2023.txt";
        std::string expected = "C:\\Users\\example\\Documents\\project_report_2023.txt";
        REQUIRE(rename_file_path(path) == expected);
    }

    SECTION("Test path with a colon at the end of the filename") {
        // Test path with a colon at the end of the filename
        std::string path = "C:\\Users\\example\\Documents\\backup:";
        std::string expected = "C:\\Users\\example\\Documents\\backup_";
        REQUIRE(rename_file_path(path) == expected);
    }

    SECTION("Test path with a colon at the start of the filename") {
        // Test path with a colon at the start of the filename
        std::string path = "C:\\Users\\example\\Documents\\:initial_setup.txt";
        std::string expected = "C:\\Users\\example\\Documents\\_initial_setup.txt";
        REQUIRE(rename_file_path(path) == expected);
    }
}