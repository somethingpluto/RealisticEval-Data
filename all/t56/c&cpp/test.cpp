TEST_CASE("findShiftJisNotGbk", "[encoding]") {
    // Call the function
    std::vector<char> result = findShiftJisNotGbk();

    // Define expected results (this should match your Python unittest)
    std::vector<char> expected = {'\x80', '\x81', /* ... */}; // Replace with actual expected values

    // Check if the result matches the expected output
    REQUIRE(result == expected);
}