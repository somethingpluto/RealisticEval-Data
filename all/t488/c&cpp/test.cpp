#include <catch2/catch_test_macros.hpp>
#include <string>
#include <optional>
#include <regex>
#include <windows.h>
#include <Shlwapi.h>

#pragma comment(lib, "Shlwapi.lib")

// Define a type alias for optional strings
using OptionalString = std::optional<std::string>;

TEST_CASE("Test Get Local IP", "[get_local_ip]") {
    SECTION("Local IP Found") {
        // Mock the output of ipconfig for a case where a local IP is found
        std::istringstream mock_output("192.168.1.10\n");
        std::streambuf* old_cout = std::cout.rdbuf(mock_output.rdbuf());

        OptionalString result = get_local_ip();
        REQUIRE(result.has_value());
        REQUIRE(*result == "192.168.1.10");

        std::cout.rdbuf(old_cout); // Restore the original stream buffer
    }

    SECTION("No Local IP Found") {
        // Mock the output of ipconfig for a case where no local IP is found
        std::istringstream mock_output("10.0.0.5\n");
        std::streambuf* old_cout = std::cout.rdbuf(mock_output.rdbuf());

        OptionalString result = get_local_ip();
        REQUIRE(!result.has_value());

        std::cout.rdbuf(old_cout); // Restore the original stream buffer
    }

    SECTION("Multiple IPs Found") {
        // Mock the output with multiple local IPs
        std::istringstream mock_output("10.0.0.5\n192.168.1.10\n");
        std::streambuf* old_cout = std::cout.rdbuf(mock_output.rdbuf());

        OptionalString result = get_local_ip();
        REQUIRE(result.has_value());
        REQUIRE(*result == "192.168.1.10");

        std::cout.rdbuf(old_cout); // Restore the original stream buffer
    }

    SECTION("Invalid Command") {
        // Simulate a case where CreateProcessA fails
        std::istringstream mock_output("");
        std::streambuf* old_cout = std::cout.rdbuf(mock_output.rdbuf());

        OptionalString result = get_local_ip();
        REQUIRE(!result.has_value());

        std::cout.rdbuf(old_cout); // Restore the original stream buffer
    }

    SECTION("Unexpected Error") {
        // Simulate an unexpected error
        std::istringstream mock_output("");
        std::streambuf* old_cout = std::cout.rdbuf(mock_output.rdbuf());

        OptionalString result = get_local_ip();
        REQUIRE(!result.has_value());

        std::cout.rdbuf(old_cout); // Restore the original stream buffer
    }
}