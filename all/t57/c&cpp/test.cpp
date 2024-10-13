class MockImage {
public:
    MOCK_METHOD(void, save, (const char*, const char*, const std::vector<std::pair<int, int>>&), (noexcept));
};

TEST_CASE("TestConvertPngToIco", "[convert_png_to_ico]") {
    SECTION("Single icon size") {
        MockImage mock_image;
        EXPECT_CALL(mock_image, save("output.ico", "ICO", Eq(std::vector<std::pair<int, int>>{{64, 64}})));

        // Mock the image loading
        CImg<unsigned char> img("source.png");
        img = mock_image; // Assign the mock image

        convertPngToIco("source.png", "output.ico", {{64, 64}});
    }

    SECTION("Multiple icon sizes") {
        MockImage mock_image;
        EXPECT_CALL(mock_image, save("output.ico", "ICO", Eq(std::vector<std::pair<int, int>>{{16, 16}, {32, 32}, {64, 64}})));

        // Mock the image loading
        CImg<unsigned char> img("source.png");
        img = mock_image; // Assign the mock image

        convertPngToIco("source.png", "output.ico", {{16, 16}, {32, 32}, {64, 64}});
    }

    SECTION("Default icon size") {
        MockImage mock_image;
        EXPECT_CALL(mock_image, save("output.ico", "ICO", Eq(std::vector<std::pair<int, int>>{{32, 32}})));

        // Mock the image loading
        CImg<unsigned char> img("source.png");
        img = mock_image; // Assign the mock image

        convertPngToIco("source.png", "output.ico");
    }

    SECTION("File handling") {
        MockImage mock_image;
        EXPECT_CALL(mock_image, save("output.ico", "ICO", Eq(std::vector<std::pair<int, int>>{{32, 32}}))).Times(1);

        // Mock the image loading
        CImg<unsigned char> img("source.png");
        img = mock_image; // Assign the mock image

        convertPngToIco("source.png", "output.ico");
    }

    SECTION("Invalid image path") {
        // Mock the image loading to throw an exception
        CImg<unsigned char> img("invalid.png");
        img.load("invalid.png").fail(); // Simulate a failure

        REQUIRE_THROWS_AS(convertPngToIco("invalid.png", "output.ico"), std::runtime_error);
    }
}