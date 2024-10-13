TEST_CASE("Test Simplify Windows Path") {
    SECTION("Simple Path") {
        CHECK(simplifyWindowsPath("C:\\Users\\User\\file.txt") == "C_Users_User_file.txt");
    }

    SECTION("Simple Path 2") {
        CHECK(simplifyWindowsPath("D:\\User\\file.txt") == "D_User_file.txt");
    }

    SECTION("Path with Spaces") {
        CHECK(simplifyWindowsPath("E:\\New Folder\\my file.docx") == "E_New Folder_my file.docx");
    }

    SECTION("Nested Directories") {
        CHECK(simplifyWindowsPath("G:\\folder1\\folder2\\folder3\\file.jpeg") == "G_folder1_folder2_folder3_file.jpeg");
    }
}