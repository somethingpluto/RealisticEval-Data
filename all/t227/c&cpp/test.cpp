TEST_CASE("Count unique colors in an image", "[image]") {
    // Test with a valid image path
    SECTION("Valid image path") {
        std::string valid_image_path = "path/to/valid/image.jpg";
        int result = count_unique_colors(valid_image_path);
        REQUIRE(result >= 0); // Ensure the result is non-negative
    }

    // Test with an invalid image path
    SECTION("Invalid image path") {
        std::string invalid_image_path = "path/to/nonexistent/image.jpg";
        int result = count_unique_colors(invalid_image_path);
        REQUIRE(result == -1); // Assuming -1 indicates an error or invalid input
    }
}