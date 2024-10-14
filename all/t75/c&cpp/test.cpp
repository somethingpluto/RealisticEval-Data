TEST_CASE("TestRenameFiles", "[rename_files]") {
    TempDir temp_dir;

    SECTION("test_basic_renaming") {
        std::vector<std::string> filenames = {"image1.png", "image2.png", "image3.png"};
        create_png_files(temp_dir.path, filenames);

        rename_files(temp_dir.path.string());

        std::vector<std::string> expected_files = {"image1001.png", "image2001.png", "image3001.png"};
        std::vector<std::string> result_files;
        for (const auto& entry : fs::directory_iterator(temp_dir.path)) {
            result_files.push_back(entry.path().filename().string());
        }
        std::sort(result_files.begin(), result_files.end());

        REQUIRE(result_files == expected_files);
    }

    SECTION("test_reset_counter_for_different_base_names") {
        std::vector<std::string> filenames = {"image1.png", "picture1.png", "image2.png", "picture2.png"};
        create_png_files(temp_dir.path, filenames);

        rename_files(temp_dir.path.string());

        std::vector<std::string> expected_files = {"image1001.png", "image2001.png", "picture1001.png", "picture2001.png"};
        std::vector<std::string> result_files;
        for (const auto& entry : fs::directory_iterator(temp_dir.path)) {
            result_files.push_back(entry.path().filename().string());
        }
        std::sort(result_files.begin(), result_files.end());

        REQUIRE(result_files == expected_files);
    }

    SECTION("test_no_png_files") {
        std::vector<std::string> filenames = {"file1.txt", "file2.jpg"};
        create_png_files(temp_dir.path, filenames);

        rename_files(temp_dir.path.string());

        std::vector<std::string> expected_files = filenames;
        std::vector<std::string> result_files;
        for (const auto& entry : fs::directory_iterator(temp_dir.path)) {
            result_files.push_back(entry.path().filename().string());
        }
        std::sort(result_files.begin(), result_files.end());

        REQUIRE(result_files == expected_files);
    }

    SECTION("test_empty_directory") {
        rename_files(temp_dir.path.string());

        std::vector<std::string> expected_files = {};
        std::vector<std::string> result_files;
        for (const auto& entry : fs::directory_iterator(temp_dir.path)) {
            result_files.push_back(entry.path().filename().string());
        }

        REQUIRE(result_files.empty());
    }

    SECTION("test_files_with_existing_numbers") {
        std::vector<std::string> filenames = {"file001.png", "file002.png", "file003.png"};
        create_png_files(temp_dir.path, filenames);

        rename_files(temp_dir.path.string());

        std::vector<std::string> expected_files = {"file001001.png", "file002001.png", "file003001.png"};
        std::vector<std::string> result_files;
        for (const auto& entry : fs::directory_iterator(temp_dir.path)) {
            result_files.push_back(entry.path().filename().string());
        }
        std::sort(result_files.begin(), result_files.end());

        REQUIRE(result_files == expected_files);
    }
}
