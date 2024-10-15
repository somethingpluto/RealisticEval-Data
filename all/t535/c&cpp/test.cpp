TEST_CASE("compressHtml", "[html]") {
    SECTION("should remove newlines and tabs") {
        std::string input = R"(
            <div>
                <p>Test paragraph.</p>
            </div>
        )";
        std::string expectedOutput = "<div><p>Test paragraph.</p></div>";
        REQUIRE(compressHtml(input) == expectedOutput);
    }

    SECTION("should replace multiple spaces with a single space") {
        std::string input = "<div>    <p>     Test with     multiple spaces.   </p></div>";
        std::string expectedOutput = "<div><p> Test with multiple spaces. </p></div>";
        REQUIRE(compressHtml(input) == expectedOutput);
    }

    SECTION("should remove spaces between HTML tags") {
        std::string input = "<div> <p>Test</p> </div>";
        std::string expectedOutput = "<div><p>Test</p></div>";
        REQUIRE(compressHtml(input) == expectedOutput);
    }

    SECTION("should handle empty input") {
        std::string input = "";
        std::string expectedOutput = "";
        REQUIRE(compressHtml(input) == expectedOutput);
    }

    SECTION("should handle HTML with only spaces and newlines") {
        std::string input = R"(
            <div>      
            </div>
        )";
        std::string expectedOutput = "<div></div>";
        REQUIRE(compressHtml(input) == expectedOutput);
    }
}