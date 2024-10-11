TEST_CASE("Simplify Windows Path", "[simplify_windows_path]") {
    CHECK(simplify_windows_path("C:\\Users\\User\\file.txt") == "Users_User_file.txt");
    CHECK(simplify_windows_path("D:\\Projects\\ProjectName\\main.cpp") == "Projects_ProjectName_main.cpp");
    CHECK(simplify_windows_path("C:\\a\\b\\c\\d.txt") == "a_b_c_d.txt");
    CHECK(simplify_windows_path("C:\\single_folder") == "single_folder");
    CHECK(simplify_windows_path("C:\\no_extension") == "no_extension");
    CHECK(simplify_windows_path("C:\\empty_path\\" )== "");
    CHECK(simplify_windows_path("C:\\trailing_backslash\\") == "trailing_backslash");
}