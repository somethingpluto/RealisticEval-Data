TEST_CASE("Read Log File", "[read_log]") {
    // Create a temporary log file for testing
    std::ofstream tempFile("temp_log.json");
    tempFile << R"({"test_acc1": 88.5, "train_loss": 0.75})";
    tempFile.close();

    auto result = read_log("temp_log.json");

    REQUIRE(result.first.size() == 1);
    REQUIRE(result.second.size() == 1);

    CHECK(result.first[0] == Approx(0.75));
    CHECK(result.second[0] == Approx(88.5));

    // Clean up the temporary file
    remove("temp_log.json");
}