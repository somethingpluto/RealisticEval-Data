TEST_CASE("Test common columns functionality", "[common-columns]") {
    // Set up a temporary directory
    const std::string test_dir = "test_dir";
    std::filesystem::create_directories(test_dir);

    SECTION("All CSV files have the same columns") {
        const std::string data1 = "A,B,C\n1,2,3";
        const std::string data2 = "A,B,C\n4,5,6";
        const std::string data3 = "A,B,C\n7,8,9";
        const std::vector<std::string> filenames = {"file1.csv", "file2.csv", "file3.csv"};
        const std::vector<std::string> datas = {data1, data2, data3};

        for (size_t i = 0; i < filenames.size(); ++i) {
            const std::string filepath = test_dir + "/" + filenames[i];
            std::ofstream file(filepath);
            file << datas[i];
        }

        REQUIRE(find_common_columns(test_dir) == std::vector<std::string>({"A", "B", "C"}));
    }

    SECTION("No common columns") {
        const std::string data1 = "A,B,C\n1,2,3";
        const std::string data2 = "D,E,F\n4,5,6";
        const std::string data3 = "G,H,I\n7,8,9";
        const std::vector<std::string> filenames = {"file1.csv", "file2.csv", "file3.csv"};
        const std::vector<std::string> datas = {data1, data2, data3};

        for (size_t i = 0; i < filenames.size(); ++i) {
            const std::string filepath = test_dir + "/" + filenames[i];
            std::ofstream file(filepath);
            file << datas[i];
        }

        REQUIRE(find_common_columns(test_dir).empty());
    }

    SECTION("Some common columns") {
        const std::string data1 = "A,B,C\n1,2,3";
        const std::string data2 = "B,C,D\n4,5,6";
        const std::string data3 = "C,D,E\n7,8,9";
        const std::vector<std::string> filenames = {"file1.csv", "file2.csv", "file3.csv"};
        const std::vector<std::string> datas = {data1, data2, data3};

        for (size_t i = 0; i < filenames.size(); ++i) {
            const std::string filepath = test_dir + "/" + filenames[i];
            std::ofstream file(filepath);
            file << datas[i];
        }

        REQUIRE(find_common_columns(test_dir) == std::vector<std::string>({"C"}));
    }

    SECTION("Mixed common and unique columns") {
        const std::string data1 = "A,B,C\n1,2,3";
        const std::string data2 = "B,C,D\n4,5,6";
        const std::string data3 = "B,C,E\n7,8,9";
        const std::vector<std::string> filenames = {"file1.csv", "file2.csv", "file3.csv"};
        const std::vector<std::string> datas = {data1, data2, data3};

        for (size_t i = 0; i < filenames.size(); ++i) {
            const std::string filepath = test_dir + "/" + filenames[i];
            std::ofstream file(filepath);
            file << datas[i];
        }

        REQUIRE(find_common_columns(test_dir) == std::vector<std::string>({"B", "C"}));
    }

    // Clean up the temporary directory
    for (const auto& entry : std::filesystem::directory_iterator(test_dir)) {
        std::filesystem::remove(entry.path());
    }
    std::filesystem::remove_all(test_dir);
}