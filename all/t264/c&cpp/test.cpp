TEST_CASE("Extract Log Entries", "[log]") {
    // Create a temporary log file with some log entries
    const std::string temp_log_file = "temp_log.txt";
    std::ofstream log_file(temp_log_file);

    if (!log_file.is_open()) {
        FAIL("Failed to create temporary log file");
    }

    log_file << "WARNING: This is a warning message\n";
    log_file << "ERROR: This is an error message\n";
    log_file << "CRITICAL: This is a critical message\n";
    log_file << "ALERT: This is an alert message\n";

    log_file.close();

    // Call the function under test
    extract_log_entries(temp_log_file);

    // Check if the output files exist and contain the correct content
    std::ifstream warning_file("WARNING.log");
    REQUIRE(warning_file.is_open());
    std::string warning_content((std::istreambuf_iterator<char>(warning_file)), std::istreambuf_iterator<char>());
    warning_file.close();
    REQUIRE(warning_content.find("WARNING: This is a warning message") != std::string::npos);

    std::ifstream error_file("ERROR.log");
    REQUIRE(error_file.is_open());
    std::string error_content((std::istreambuf_iterator<char>(error_file)), std::istreambuf_iterator<char>());
    error_file.close();
    REQUIRE(error_content.find("ERROR: This is an error message") != std::string::npos);

    std::ifstream critical_file("CRITICAL.log");
    REQUIRE(critical_file.is_open());
    std::string critical_content((std::istreambuf_iterator<char>(critical_file)), std::istreambuf_iterator<char>());
    critical_file.close();
    REQUIRE(critical_content.find("CRITICAL: This is a critical message") != std::string::npos);

    std::ifstream alert_file("ALERT.log");
    REQUIRE(alert_file.is_open());
    std::string alert_content((std::istreambuf_iterator<char>(alert_file)), std::istreambuf_iterator<char>());
    alert_file.close();
    REQUIRE(alert_content.find("ALERT: This is an alert message") != std::string::npos);

    // Clean up the temporary log file
    std::remove(temp_log_file.c_str());
}