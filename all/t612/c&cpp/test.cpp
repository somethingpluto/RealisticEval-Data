TEST_CASE_METHOD(TestFindAndReplace, "Basic find and replace") {
    auto file_path = temp_dir / "testfile.txt";
    std::ofstream(file_path) << "Hello World\nGoodbye World\n";

    find_and_replace_in_file(file_path.string(), "World", "Java");

    std::ifstream ifs(file_path);
    std::string result((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    REQUIRE(result == "Hello Java\nGoodbye Java\n");
}

TEST_CASE_METHOD(TestFindAndReplace, "No occurrences of the search string") {
    auto file_path = temp_dir / "testfile.txt";
    std::ofstream(file_path) << "Hello World\nGoodbye World\n";

    find_and_replace_in_file(file_path.string(), "Python", "Java");

    std::ifstream ifs(file_path);
    std::string result((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    REQUIRE(result == "Hello World\nGoodbye World\n");
}

TEST_CASE_METHOD(TestFindAndReplace, "Multiple occurrences in a single line") {
    auto file_path = temp_dir / "testfile.txt";
    std::ofstream(file_path) << "Hello World World\nGoodbye World\n";

    find_and_replace_in_file(file_path.string(), "World", "Java");

    std::ifstream ifs(file_path);
    std::string result((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    REQUIRE(result == "Hello Java Java\nGoodbye Java\n");
}

TEST_CASE_METHOD(TestFindAndReplace, "Replace with an empty string") {
    auto file_path = temp_dir / "testfile.txt";
    std::ofstream(file_path) << "Hello World\nGoodbye World\n";

    find_and_replace_in_file(file_path.string(), "World", "");

    std::ifstream ifs(file_path);
    std::string result((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    REQUIRE(result == "Hello \nGoodbye \n");
}

TEST_CASE_METHOD(TestFindAndReplace, "Empty file") {
    auto file_path = temp_dir / "testfile.txt";
    std::ofstream(file_path) << "\n";

    find_and_replace_in_file(file_path.string(), "World", "Java");

    std::ifstream ifs(file_path);
    std::string result((std::istreambuf_iterator<char>(ifs)), std::istreambuf_iterator<char>());
    REQUIRE(result == "\n");
}