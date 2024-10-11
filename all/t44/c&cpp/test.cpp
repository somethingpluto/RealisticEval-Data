TEST_CASE("Align lines left", "[align_lines_left]") {
    SECTION("Both strings have the same length") {
        auto result = align_lines_left("hello", "world");
        REQUIRE(std::get<0>(result) == "hello");
        REQUIRE(std::get<1>(result) == "world");
    }

    SECTION("First string is longer") {
        auto result = align_lines_left("hello", "hi");
        REQUIRE(std::get<0>(result) == "hello");
        REQUIRE(std::get<1>(result) == "hi   ");
    }

    SECTION("Second string is longer") {
        auto result = align_lines_left("hi", "hello");
        REQUIRE(std::get<0>(result) == " hi  ");
        REQUIRE(std::get<1>(result) == "hello");
    }
}