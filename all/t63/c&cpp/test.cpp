TEST_CASE("Dataframe to Markdown Conversion", "[dataframe_to_markdown]") {
    // Create a sample DataFrame
    pandas::DataFrame df = {{"Name", {"Alice", "Bob"}},
                            {"Age", {25, 30}}};

    // Specify the output MD file path
    std::string md_path = "output.md";

    // Call the function with the sample DataFrame and output path
    std::string result = dataframe_to_markdown(df, md_path);

    // Check if the result matches the expected markdown content
    REQUIRE(result == "| Name | Age |\n| --- | --- |\n| Alice | 25 |\n| Bob | 30 |\n");
}