TEST_CASE("Test Im2Col Function") {
    SECTION("Single channel, no padding, stride 1") {
        Array3i image(1, 4, 4);
        image << 1, 2, 3, 4,
                 5, 6, 7, 8,
                 9, 10, 11, 12,
                 13, 14, 15, 16;

        int filter_height = 2;
        int filter_width = 2;
        int stride = 1;
        int padding = 0;

        MatrixXd expected_output(4, 9);
        expected_output << 1, 2, 3, 5, 6, 7, 9, 10, 11,
                           2, 3, 4, 6, 7, 8, 10, 11, 12,
                           5, 6, 7, 9, 10, 11, 13, 14, 15,
                           6, 7, 8, 10, 11, 12, 14, 15, 16;

        MatrixXd output = im2col(image, filter_height, filter_width, stride, padding);

        REQUIRE(output.rows() == expected_output.rows());
        REQUIRE(output.cols() == expected_output.cols());
        REQUIRE_THAT(output, Catch::Matchers::WithinAbs(expected_output, 1e-6));
    }

    SECTION("Single channel, no padding, stride 2") {
        Array3i image(1, 4, 4);
        image << 1, 2, 3, 4,
                 5, 6, 7, 8,
                 9, 10, 11, 12,
                 13, 14, 15, 16;

        int filter_height = 2;
        int filter_width = 2;
        int stride = 2;
        int padding = 0;

        MatrixXd expected_output(4, 4);
        expected_output << 1, 3, 9, 11,
                           2, 4, 10, 12,
                           5, 7, 13, 15,
                           6, 8, 14, 16;

        MatrixXd output = im2col(image, filter_height, filter_width, stride, padding);

        REQUIRE(output.rows() == expected_output.rows());
        REQUIRE(output.cols() == expected_output.cols());
        REQUIRE_THAT(output, Catch::Matchers::WithinAbs(expected_output, 1e-6));
    }

    SECTION("Multi-channel, no padding, stride 1") {
        Array3i image(2, 3, 3);
        image << 1, 2, 3,
                 4, 5, 6,
                 7, 8, 9,
                 9, 8, 7,
                 6, 5, 4,
                 3, 2, 1;

        int filter_height = 2;
        int filter_width = 2;
        int stride = 1;
        int padding = 0;

        MatrixXd expected_output(8, 4);
        expected_output << 1, 2, 4, 5,
                           2, 3, 5, 6,
                           4, 5, 7, 8,
                           5, 6, 8, 9,
                           9, 8, 6, 5,
                           8, 7, 5, 4,
                           6, 5, 3, 2,
                           5, 4, 2, 1;

        MatrixXd output = im2col(image, filter_height, filter_width, stride, padding);

        REQUIRE(output.rows() == expected_output.rows());
        REQUIRE(output.cols() == expected_output.cols());
        REQUIRE_THAT(output, Catch::Matchers::WithinAbs(expected_output, 1e-6));
    }
}