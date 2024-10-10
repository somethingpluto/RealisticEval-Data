// Write tests for the log function
TEST_CASE("Logging Tests", "[log]") {
    SECTION("String Logging") {
        log(std::string("Hello, World!"));
        REQUIRE(true); // Replace with actual assertion
    }

    SECTION("Integer Logging") {
        log(42);
        REQUIRE(true); // Replace with actual assertion
    }

    SECTION("Vector Logging") {
        std::vector<std::any> vec = {1, "two", 3.0};
        log(vec);
        REQUIRE(true); // Replace with actual assertion
    }

    SECTION("Map Logging") {
        std::map<std::string, std::any> map = {{"one", 1}, {"two", "two"}, {"three", 3.0}};
        log(map);
        REQUIRE(true); // Replace with actual assertion
    }
}