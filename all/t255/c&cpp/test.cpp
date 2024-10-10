TEST_CASE("Convert Image to Bits", "[image_conversion]") {
    std::string image_path = "path/to/test/image.png"; // Replace with actual test image path

    // Call the function under test
    auto bits = MockImageConverter::convert_image_to_bits(image_path);

    // Define expected results
    std::vector<int> expected_bits = {0, 1, 0, 1}; // Replace with actual expected bits

    // Check if the result matches the expected output
    REQUIRE(bits == expected_bits);
}