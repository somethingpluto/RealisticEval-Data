TEST_CASE_METHOD(TestGetMinDistance, "Test basic functionality with expected input") {
    content = "hello world\napple banana apple\norange apple banana";
    setup_temp_file();

    auto [line_number, distance] = get_min_seq_num_and_distance(temp_file_path, "apple", "banana");
    REQUIRE((line_number, distance) == std::make_pair(2, 1));

    teardown_temp_file();
}

TEST_CASE_METHOD(TestGetMinDistance, "Test case where one or both words are not present") {
    content = "apple orange pear\norange pear apple";
    setup_temp_file();

    auto [line_number, distance] = get_min_seq_num_and_distance(temp_file_path, "apple", "banana");
    REQUIRE((line_number, distance) == std::make_pair(-1, std::numeric_limits<int>::max()));

    teardown_temp_file();
}

TEST_CASE_METHOD(TestGetMinDistance, "Test an empty file") {
    content = "";
    setup_temp_file();

    auto [line_number, distance] = get_min_seq_num_and_distance(temp_file_path, "apple", "banana");
    REQUIRE((line_number, distance) == std::make_pair(-1, std::numeric_limits<int>::max()));

    teardown_temp_file();
}

TEST_CASE_METHOD(TestGetMinDistance, "Test multiple lines with varying distances between words") {
    content = "apple banana\napple orange orange banana\napple orange orange orange banana";
    setup_temp_file();

    auto [line_number, distance] = get_min_seq_num_and_distance(temp_file_path, "apple", "banana");
    REQUIRE((line_number, distance) == std::make_pair(1, 1));

    teardown_temp_file();
}