TEST_CASE("TestSimplifyWindowsPath") {

    SECTION("should simplify a simple path") {
        REQUIRE(simplify_windows_path("C:\\Users\\User\\file.txt") == "C_Users_User_file.txt");
    }

    SECTION("should simplify another simple path") {
        REQUIRE(simplify_windows_path("D:\\User\\file.txt") == "D_User_file.txt");
    }

    SECTION("should simplify a path with spaces") {
        REQUIRE(simplify_windows_path("E:\\New Folder\\my file.docx") == "E_New Folder_my file.docx");
    }

    SECTION("should simplify a nested directory path") {
        REQUIRE(simplify_windows_path("G:\\folder1\\folder2\\folder3\\file.jpeg") == "G_folder1_folder2_folder3_file.jpeg");
    }
}