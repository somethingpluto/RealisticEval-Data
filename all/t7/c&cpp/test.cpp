#define CATCH_CONFIG_MAIN
#include <catch2/catch.hpp>
#include <sstream>
#include <iostream>
#include "Logger.h"  // Assuming the logger implementation is in this file

TEST_CASE("Logger tests", "[logger]") {
    std::string loggerName = "test_logger";
    std::stringstream buffer;
    Logger logger(loggerName, DEBUG);

    // Redirect cout to buffer
    auto* oldBuf = std::cout.rdbuf(buffer.rdbuf());

    SECTION("Debug logging") {
        std::string message = "This is a debug message";
        logger.log(DEBUG, message);
        std::string output = buffer.str();
        REQUIRE(output.find(message) != std::string::npos);
    }

    SECTION("Info logging") {
        buffer.str(""); // Clear buffer
        std::string message = "This is an info message";
        logger.log(INFO, message);
        std::string output = buffer.str();
        REQUIRE(output.find(message) != std::string::npos);
    }

    SECTION("Warning logging") {
        buffer.str(""); // Clear buffer
        std::string message = "This is a warning message";
        logger.log(WARNING, message);
        std::string output = buffer.str();
        REQUIRE(output.find(message) != std::string::npos);
    }

    SECTION("Error logging") {
        buffer.str(""); // Clear buffer
        std::string message = "This is an error message";
        logger.log(ERROR, message);
        std::string output = buffer.str();
        REQUIRE(output.find(message) != std::string::npos);
    }

    SECTION("Critical logging") {
        buffer.str(""); // Clear buffer
        std::string message = "This is a critical message";
        logger.log(CRITICAL, message);
        std::string output = buffer.str();
        REQUIRE(output.find(message) != std::string::npos);
    }

    // Reset cout to original buffer
    std::cout.rdbuf(oldBuf);
}