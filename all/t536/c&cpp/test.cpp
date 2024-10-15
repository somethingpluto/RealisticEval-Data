std::string getDate() {
    // Normally would return the actual date; here we simulate for testing
    return "October 1, 2024"; 
}

TEST_CASE("getDate", "[date]") {
    SECTION("returns date in 'Month Day, Year' format") {
        REQUIRE(getDate() == "October 1, 2024");
    }

    SECTION("returns correct year") {
        REQUIRE(getDate().find("2024") != std::string::npos);
    }

    SECTION("returns correct month") {
        REQUIRE(getDate().find("October") != std::string::npos);
    }

    SECTION("returns correct day") {
        REQUIRE(getDate().find("1") != std::string::npos);
    }

    SECTION("returns date as a string") {
        REQUIRE(typeid(getDate()).name() == typeid(std::string).name());
    }

    SECTION("does not return undefined") {
        REQUIRE_FALSE(getDate().empty());
    }
}