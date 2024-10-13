TEST_CASE("Test align_lines_left function", "[align_lines_left]") {
    SECTION("Equal length strings") {
        std::string str1 = "Hello";
        std::string str2 = "World";
        std::string expected_str1 = "Hello";
        std::string expected_str2 = "World";
        auto [aligned_str1, aligned_str2] = align_lines_left(str1, str2);
        REQUIRE(aligned_str1 == expected_str1);
        REQUIRE(aligned_str2 == expected_str2);
    }

    SECTION("First string longer") {
        std::string str1 = "Hello, World!";
        std::string str2 = "Hi";
        std::string expected_str1 = "Hello, World!";
        std::string expected_str2 = "Hi           ";  // 14 spaces after "Hi"
        auto [aligned_str1, aligned_str2] = align_lines_left(str1, str2);
        REQUIRE(aligned_str1 == expected_str1);
        REQUIRE(aligned_str2 == expected_str2);
    }

    SECTION("Second string longer") {
        std::string str1 = "Hey";
        std::string str2 = "Goodbye, friend!";
        std::string expected_str1 = "Hey             ";  // 15 spaces after "Hey"
        std::string expected_str2 = "Goodbye, friend!";
        auto [aligned_str1, aligned_str2] = align_lines_left(str1, str2);
        REQUIRE(aligned_str1 == expected_str1);
        REQUIRE(aligned_str2 == expected_str2);
    }

    SECTION("Empty first string") {
        std::string str1 = "";
        std::string str2 = "World";
        std::string expected_str1 = "     ";  // 5 spaces
        std::string expected_str2 = "World";
        auto [aligned_str1, aligned_str2] = align_lines_left(str1, str2);
        REQUIRE(aligned_str1 == expected_str1);
        REQUIRE(aligned_str2 == expected_str2);
    }

    SECTION("Empty second string") {
        std::string str1 = "Hello";
        std::string str2 = "";
        std::string expected_str1 = "Hello";
        std::string expected_str2 = "     ";  // 5 spaces
        auto [aligned_str1, aligned_str2] = align_lines_left(str1, str2);
        REQUIRE(aligned_str1 == expected_str1);
        REQUIRE(aligned_str2 == expected_str2);
    }

    SECTION("Both strings empty") {
        std::string str1 = "";
        std::string str2 = "";
        std::string expected_str1 = "";
        std::string expected_str2 = "";
        auto [aligned_str1, aligned_str2] = align_lines_left(str1, str2);
        REQUIRE(aligned_str1 == expected_str1);
        REQUIRE(aligned_str2 == expected_str2);
    }

    SECTION("Strings with spaces") {
        std::string str1 = "Hello ";
        std::string str2 = "World  ";
        std::string expected_str1 = "Hello  ";
        std::string expected_str2 = "World  ";
        auto [aligned_str1, aligned_str2] = align_lines_left(str1, str2);
        REQUIRE(aligned_str1 == expected_str1);
        REQUIRE(aligned_str2 == expected_str2);
    }
}