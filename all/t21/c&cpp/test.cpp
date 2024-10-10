TEST_CASE("Compare files with no differences", "[compare_files]") {
    std::ofstream file1("temp_file1.txt");
    file1 << "Hello\nWorld";
    file1.close();

    std::ofstream file2("temp_file2.txt");
    file2 << "Hello\nWorld";
    file2.close();

    auto result = compare_files("temp_file1.txt", "temp_file2.txt");

    REQUIRE(result.empty());

    remove("temp_file1.txt");
    remove("temp_file2.txt");
}

TEST_CASE("Compare files with differences", "[compare_files]") {
    std::ofstream file1("temp_file1.txt");
    file1 << "Hello\nWorld";
    file1.close();

    std::ofstream file2("temp_file2.txt");
    file2 << "Hello\nUniverse";
    file2.close();

    auto result = compare_files("temp_file1.txt", "temp_file2.txt");

    REQUIRE(result.size() == 4);
    REQUIRE(result[0] == "World");
    REQUIRE(result[1] == "Universe");

    remove("temp_file1.txt");
    remove("temp_file2.txt");
}