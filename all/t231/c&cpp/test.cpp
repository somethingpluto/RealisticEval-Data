TEST_CASE("readLog function tests") {
    
    // Create a temporary file for testing
    std::string testFilePath = "dummy_path.json";

    SECTION("reads correctly formatted JSON lines") {
        std::ofstream outFile(testFilePath);
        outFile << "{\"test_acc1\": 88.5, \"train_loss\": 0.75}\n"
                << "{\"test_acc1\": 89.0, \"train_loss\": 0.70}";
        outFile.close();

        auto [trainLossList, testAcc1List] = readLog(testFilePath);
        REQUIRE(trainLossList == std::vector<double>{0.75, 0.70});
        REQUIRE(testAcc1List == std::vector<double>{88.5, 89.0});
    }

    SECTION("reads correctly formatted JSON lines - single entry") {
        std::ofstream outFile(testFilePath);
        outFile << "{\"test_acc1\": 88.5, \"train_loss\": 0.75}";
        outFile.close();

        auto [trainLossList, testAcc1List] = readLog(testFilePath);
        REQUIRE(trainLossList == std::vector<double>{0.75});
        REQUIRE(testAcc1List == std::vector<double>{88.5});
    }

    SECTION("reads an empty file") {
        std::ofstream outFile(testFilePath);
        outFile.close(); // Create an empty file

        auto [trainLossList, testAcc1List] = readLog(testFilePath);
        REQUIRE(trainLossList.empty());
        REQUIRE(testAcc1List.empty());
    }

    SECTION("handles partial data entries") {
        std::ofstream outFile(testFilePath);
        outFile << "{\"test_acc1\": 88.5, \"train_loss\": 0.75}\n"
                << "{\"test_acc1\": 90.0, \"train_loss\": 0.75, \"f1\": 0.91}"; // Missing train_loss
        outFile.close();

        auto [trainLossList, testAcc1List] = readLog(testFilePath);
        REQUIRE(trainLossList == std::vector<double>{0.75, 0.75}); // Only one complete entry
        REQUIRE(testAcc1List == std::vector<double>{88.5, 90.0});
    }
    
    // Clean up the test file after tests
    remove(testFilePath.c_str());
}
