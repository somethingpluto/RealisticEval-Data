TEST_CASE("TestExtractLogEntries", "[log]") {
    const std::string log_file_path = "test_log.log";

    SECTION("setUp") {
        std::vector<std::string> log_contents = {
            "INFO: This is an informational message.\n",
            "WARNING: This is a warning message.\n",
            "ERROR: This is an error message.\n",
            "CRITICAL: This is a critical message.\n",
            "ALERT: This is an alert message.\n"
        };
        std::ofstream log_file(log_file_path);
        if (!log_file.is_open()) {
            FAIL("Failed to create the log file.");
        }
        log_file << std::string(log_contents.begin(), log_contents.end());
        log_file.close();
    }

    SECTION("test_no_logs_of_certain_levels") {
        std::ofstream log_file(log_file_path);
        if (!log_file.is_open()) {
            FAIL("Failed to create the log file.");
        }
        log_file << "INFO: This is another informational message.\n";
        log_file.close();

        extract_log_entries(log_file_path);

        for (const auto& level : {"WARNING", "ERROR", "CRITICAL", "ALERT"}) {
            std::ifstream outfile(level + "_logs.txt");
            if (!outfile.is_open()) {
                FAIL("Failed to open the output file: " + level + "_logs.txt");
            }
            std::string content((std::istreambuf_iterator<char>(outfile)), std::istreambuf_iterator<char>());
            REQUIRE(content.empty());
        }
    }

    SECTION("test_file_not_found") {
        extract_log_entries("nonexistent.log");
        for (const auto& level : {"WARNING", "ERROR", "CRITICAL", "ALERT"}) {
            std::ifstream outfile(level + "_logs.txt");
            if (!outfile.is_open()) {
                FAIL("Failed to open the output file: " + level + "_logs.txt");
            }
            std::string content((std::istreambuf_iterator<char>(outfile)), std::istreambuf_iterator<char>());
            REQUIRE(content.empty());
        }
    }

    SECTION("test_empty_log_file") {
        std::ofstream log_file(log_file_path);
        if (!log_file.is_open()) {
            FAIL("Failed to create the log file.");
        }
        log_file.close();

        extract_log_entries(log_file_path);

        for (const auto& level : {"WARNING", "ERROR", "CRITICAL", "ALERT"}) {
            std::ifstream outfile(level + "_logs.txt");
            if (!outfile.is_open()) {
                FAIL("Failed to open the output file: " + level + "_logs.txt");
            }
            std::string content((std::istreambuf_iterator<char>(outfile)), std::istreambuf_iterator<char>());
            REQUIRE(content.empty());
        }
    }

    SECTION("test_mixed_content_log_file") {
        std::ofstream log_file(log_file_path);
        if (!log_file.is_open()) {
            FAIL("Failed to create the log file.");
        }
        log_file << "INFO: Some info.\n"
                 << "WARNING: Watch out!\n"
                 << "DEBUG: Debugging.\n"
                 << "ERROR: Oops!\n"
                 << "CRITICAL: Failed badly.\n"
                 << "ALERT: High alert!\n"
                 << "INFO: More info.\n";
        log_file.close();

        extract_log_entries(log_file_path);

        for (const auto& level : {"WARNING", "ERROR", "CRITICAL", "ALERT"}) {
            std::ifstream outfile(level + "_logs.txt");
            if (!outfile.is_open()) {
                FAIL("Failed to open the output file: " + level + "_logs.txt");
            }
            std::string content((std::istreambuf_iterator<char>(outfile)), std::istreambuf_iterator<char>());
            REQUIRE(content.find(level) != std::string::npos);
        }
    }
}