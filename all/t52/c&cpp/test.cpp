#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>
#include "your_code_file.hpp" // Include the file where renameFilePath is defined

TEST_CASE("Rename file path tests", "[renameFilePath]") {
    SECTION("Rename with colon in filename") {
        std::string path = "C:\\Users\\example\\Documents\\report:2023.txt";
        std::string expected = "C:\\Users\\example\\Documents\\report_2023.txt";
        REQUIRE(renameFilePath(path) == expected);
    }

    SECTION("Rename without colon in filename") {
        std::string path = "C:\\Users\\example\\Documents\\report2023.txt";
        std::string expected = "C:\\Users\\example\\Documents\\report2023.txt";
        REQUIRE(renameFilePath(path) == expected);
    }

    SECTION("Rename with multiple colons in filename") {
        std::string path = "C:\\Users\\example\\Documents\\project:report:2023.txt";
        std::string expected = "C:\\Users\\example\\Documents\\project_report_2023.txt";
        REQUIRE(renameFilePath(path) == expected);
    }

    SECTION("Rename with colon at end of filename") {
        std::string path = "C:\\Users\\example\\Documents\\backup:";
        std::string expected = "C:\\Users\\example\\Documents\\backup_";
        REQUIRE(renameFilePath(path) == expected);
    }

    SECTION("Rename with colon at start of filename") {
        std::string path = "C:\\Users\\example\\Documents\\:initial_setup.txt";
        std::string expected = "C:\\Users\\example\\Documents\\_initial_setup.txt";
        REQUIRE(renameFilePath(path) == expected);
    }
}