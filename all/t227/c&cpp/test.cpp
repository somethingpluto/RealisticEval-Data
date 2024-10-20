TEST_CASE("Test count_unique_colors function", "[count_unique_colors]") {
    SECTION("Test case 1") {
        std::string picture_path = R"(E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase01.png)";
        int expected_color_num = 1;
        int output = count_unique_colors(picture_path);
        REQUIRE(output == expected_color_num);
    }

    SECTION("Test case 2") {
        std::string picture_path = R"(E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase02.png)";
        int expected_color_num = 2;
        int output = count_unique_colors(picture_path);
        REQUIRE(output == expected_color_num);
    }

    SECTION("Test case 3") {
        std::string picture_path = R"(E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase03.png)";
        int expected_color_num = 3;
        int output = count_unique_colors(picture_path);
        REQUIRE(output == expected_color_num);
    }

    SECTION("Test case 4") {
        std::string picture_path = R"(E:\code\code_back\python_project\RealisticEval-Data\envs\python\test_case\t227\testcase04.png)";
        int expected_color_num = 466;
        int output = count_unique_colors(picture_path);
        REQUIRE(output == expected_color_num);
    }
}