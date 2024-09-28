#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <string>

/* Function to simplify Windows paths -- assumed to be provided */
std::string simplify_windows_path(const std::string& path) {
    size_t pos = path.find(':');
    std::string simplified_drive;
    std::string path_without_drive;

    if (pos != std::string::npos) {
        simplified_drive = path.substr(0, pos) + "_";
        path_without_drive = path.substr(pos + 1);
    } else {
        path_without_drive = path;
    }

    for (auto& ch : path_without_drive) {
        if (ch == '\\') {
            ch = '_';
        }
    }

    if (!path_without_drive.empty() && path_without_drive.front() == '_') {
        path_without_drive.erase(0, 1);
    }
    if (!path_without_drive.empty() && path_without_drive.back() == '_') {
        path_without_drive.pop_back();
    }

    std::string final_path = simplified_drive + path_without_drive;
    return final_path;
}

/* Test cases */
TEST_CASE("Simplify Windows Path") {
    SECTION("Simple Path") {
        REQUIRE(simplify_windows_path("C:\\Users\\User\\file.txt") == "C_Users_User_file.txt");
    }

    SECTION("Path with Spaces") {
        REQUIRE(simplify_windows_path("E:\\New Folder\\my file.docx") == "E_New Folder_my file.docx");
    }

    SECTION("Path with Special Characters") {
        REQUIRE(simplify_windows_path("D:\\question\\new-year@2020\\report#1.pdf") == "D_question_new-year@2020_report#1.pdf");
    }

    SECTION("Nested Directories") {
        REQUIRE(simplify_windows_path("G:\\folder1\\folder2\\folder3\\file.jpeg") == "G_folder1_folder2_folder3_file.jpeg");
    }
}