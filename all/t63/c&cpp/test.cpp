TEST_CASE("Test DataFrame to Markdown Conversion") {
    SECTION("Test df_to_str") {
        // Test that the function writes the correct markdown to a file
        std::vector<std::vector<std::string>> data = {{"Alice", "25"}, {"Bob", "30"}};
        std::vector<std::string> columns = {"Name", "Age"};
        DataFrame df(data, columns);

        std::string expected_markdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    25 |\n| Bob    |    30 |";
        std::string result = dataframe_to_markdown(df, "dummy_path.md");
        REQUIRE(result == expected_markdown);
    }

    SECTION("Test empty dataframe") {
        // Test how the function handles an empty DataFrame
        std::vector<std::vector<std::string>> data = {};
        std::vector<std::string> columns = {};
        DataFrame df(data, columns);

        std::string expected_markdown = "";
        std::string result = dataframe_to_markdown(df, "dummy_path.md");
        REQUIRE(result == expected_markdown);
    }

    SECTION("Test single row dataframe") {
        // Test with a DataFrame that contains only one row
        std::vector<std::vector<std::string>> data = {{"Alice", "30"}};
        std::vector<std::string> columns = {"Name", "Age"};
        DataFrame df(data, columns);

        std::string expected_markdown = "| Name   |   Age |\n|:-------|------:|\n| Alice  |    30 |";
        std::string result = dataframe_to_markdown(df, "dummy_path.md");
        REQUIRE(result == expected_markdown);
    }

    SECTION("Test non-string columns") {
        // Test with non-string question types in the DataFrame
        std::vector<std::vector<std::string>> data = {{"Alice", "25", "5.5"}, {"Bob", "30", "6.0"}};
        std::vector<std::string> columns = {"Name", "Age", "Height"};
        DataFrame df(data, columns);

        std::string expected_markdown = "| Name   |   Age |   Height |\n|:-------|------:|---------:|\n| Alice  |    25 |      5.5 |\n| Bob    |    30 |      6   |";
        std::string result = dataframe_to_markdown(df, "dummy_path.md");
        REQUIRE(result == expected_markdown);
    }

    SECTION("Test special characters") {
        // Test handling of special characters in DataFrame
        std::vector<std::vector<std::string>> data = {{"Alice", "Good@Work!"}, {"Bob", "Excellent & Commendable"}};
        std::vector<std::string> columns = {"Name", "Comments"};
        DataFrame df(data, columns);

        std::string expected_markdown = "| Name   | Comments                |\n|:-------|:------------------------|\n| Alice  | Good@Work!              |\n| Bob    | Excellent & Commendable |";
        std::string result = dataframe_to_markdown(df, "dummy_path.md");
        REQUIRE(result == expected_markdown);
    }
}