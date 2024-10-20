TEST_CASE_METHOD(TestDirectoryOperations, "Copy empty directory") {
    copy_directory(source_dir, target_dir);

    REQUIRE(fs::exists(target_dir));
    REQUIRE(fs::is_directory(target_dir));
    REQUIRE(fs::is_empty(target_dir));
}

TEST_CASE_METHOD(TestDirectoryOperations, "Copy directory with files") {
    std::string test_file = (fs::path(source_dir) / "testFile.txt").string();
    {
        std::ofstream f(test_file);
        f << "Sample content";
    }

    copy_directory(source_dir, target_dir);

    std::string copied_file = (fs::path(target_dir) / "testFile.txt").string();
    REQUIRE(fs::exists(copied_file));
    REQUIRE(fs::file_size(test_file) == fs::file_size(copied_file));
}

TEST_CASE_METHOD(TestDirectoryOperations, "Non-existent source directory") {
    std::string non_existent_dir = "nonExistentDir";

    REQUIRE_THROWS_AS(copy_directory(non_existent_dir, target_dir), std::invalid_argument);
}

TEST_CASE_METHOD(TestDirectoryOperations, "Copy directory with subdirectories") {
    std::string sub_dir = (fs::path(source_dir) / "subDir").string();
    fs::create_directories(sub_dir);
    std::string test_file = (fs::path(sub_dir) / "testFile.txt").string();
    {
        std::ofstream f(test_file);
        f << "Sample content in subdirectory";
    }

    copy_directory(source_dir, target_dir);

    std::string copied_sub_dir = (fs::path(target_dir) / "subDir").string();
    std::string copied_file = (fs::path(copied_sub_dir) / "testFile.txt").string();

    REQUIRE(fs::exists(copied_sub_dir));
    REQUIRE(fs::exists(copied_file));
}

TEST_CASE_METHOD(TestDirectoryOperations, "Overwrite file in target directory") {
    std::string test_file = (fs::path(source_dir) / "testFile.txt").string();
    {
        std::ofstream f(test_file);
        f << "Source content";
    }

    std::string target_file = (fs::path(target_dir) / "testFile.txt").string();
    {
        std::ofstream f(target_file);
        f << "Target content";
    }

    copy_directory(source_dir, target_dir);

    std::string copied_file = (fs::path(target_dir) / "testFile.txt").string();
    REQUIRE(fs::exists(copied_file));

    std::ifstream f(copied_file);
    std::string copied_content((std::istreambuf_iterator<char>(f)), std::istreambuf_iterator<char>());

    REQUIRE(copied_content == "Source content");
}