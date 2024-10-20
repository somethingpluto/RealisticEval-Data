TEST_CASE("TestConvertImageToBits", "[image]") {
    SECTION("All White Image") {
        const char* filename = "all_white.png";
        create_and_save_image("1", {4, 4}, 255, filename);
        std::vector<int> expected_bits = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
        std::vector<int> result = convert_image_to_bits(filename);
        REQUIRE(result == expected_bits);
    }

    SECTION("All Black Image") {
        const char* filename = "all_black.png";
        create_and_save_image("1", {4, 4}, 0, filename);
        std::vector<int> expected_bits = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
        std::vector<int> result = convert_image_to_bits(filename);
        REQUIRE(result == expected_bits);
    }

    SECTION("Checkerboard Image") {
        const char* filename = "checkerboard.png";
        create_and_save_image("1", {4, 4}, 0, filename);

        // Load the image and modify pixels
        int width, height, channels;
        unsigned char* data = stbi_load(filename, &width, &height, &channels, 1);
        for (int y = 0; y < height; ++y) {
            for (int x = 0; x < width; ++x) {
                if ((x + y) % 2 == 0) {
                    data[y * width + x] = 255;
                }
            }
        }
        stbi_write_png(filename, width, height, 1, data, width);
        stbi_image_free(data);

        std::vector<int> expected_bits = {1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1};
        std::vector<int> result = convert_image_to_bits(filename);
        REQUIRE(result == expected_bits);
    }

    SECTION("Horizontal Stripes Image") {
        const char* filename = "horizontal_stripes.png";
        create_and_save_image("1", {4, 4}, 0, filename);

        // Load the image and modify pixels
        int width, height, channels;
        unsigned char* data = stbi_load(filename, &width, &height, &channels, 1);
        for (int y = 0; y < height; ++y) {
            for (int x = 0; x < width; ++x) {
                if (y % 2 == 0) {
                    data[y * width + x] = 255;
                }
            }
        }
        stbi_write_png(filename, width, height, 1, data, width);
        stbi_image_free(data);

        std::vector<int> expected_bits = {1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0};
        std::vector<int> result = convert_image_to_bits(filename);
        REQUIRE(result == expected_bits);
    }

    SECTION("Vertical Stripes Image") {
        const char* filename = "vertical_stripes.png";
        create_and_save_image("1", {4, 4}, 0, filename);

        // Load the image and modify pixels
        int width, height, channels;
        unsigned char* data = stbi_load(filename, &width, &height, &channels, 1);
        for (int y = 0; y < height; ++y) {
            for (int x = 0; x < width; ++x) {
                if (x % 2 == 0) {
                    data[y * width + x] = 255;
                }
            }
        }
        stbi_write_png(filename, width, height, 1, data, width);
        stbi_image_free(data);

        std::vector<int> expected_bits = {1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0};
        std::vector<int> result = convert_image_to_bits(filename);
        REQUIRE(result == expected_bits);
    }
}