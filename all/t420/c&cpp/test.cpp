TEST_CASE("Test Get Min Distance") {
    SECTION("Simple case") {
        std::vector<std::string> lines = {
            "hello world",
            "hello hello world",
            "world hello"
        };
        REQUIRE(get_min_distance("dummy_file.txt", "hello", "world") == std::make_pair(0, 1));
    }

    SECTION("Multiple lines") {
        std::vector<std::string> lines = {
            "hello planet",
            "world hello planet",
            "hello world planet"
        };
        REQUIRE(get_min_distance("dummy_file.txt", "hello", "world") == std::make_pair(1, 1));
    }

    SECTION("Large distance") {
        std::vector<std::string> lines = {
            "hello a b c d e f g h i j k l m n o p q r s t u v w x y z world"
        };
        REQUIRE(get_min_distance("dummy_file.txt", "hello", "world") == std::make_pair(0, 27));
    }

    SECTION("Adjacent words") {
        std::vector<std::string> lines = {
            "hello world",
            "hello hello world world",
            "world hello"
        };
        REQUIRE(get_min_distance("dummy_file.txt", "hello", "world") == std::make_pair(0, 1));
    }
}