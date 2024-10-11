TEST_CASE("extract_json returns an empty string for input without '{'") {
    std::string input = "No braces here";
    REQUIRE(extract_json(input) == "");
}

TEST_CASE("extract_json extracts a single JSON object") {
    std::string input = "Here is some text before { \"key\": \"value\" } and some text after.";
    REQUIRE(extract_json(input) == "{ \"key\": \"value\" }");
}

TEST_CASE("extract_json handles nested JSON objects") {
    std::string input = "Some text { \"outer\": { \"inner\": \"value\" } } more text.";
    REQUIRE(extract_json(input) == "{ \"outer\": { \"inner\": \"value\" } }");
}

TEST_CASE("extract_json returns an empty string for unmatched braces") {
    std::string input = "Here is an incomplete JSON { \"key\": \"value\" ";
    REQUIRE(extract_json(input) == "");
}

TEST_CASE("extract_json returns the correct JSON when multiple braces are present") {
    std::string input = "Start { { \"key\": \"value\" } and some other text { \"another\": \"object\" }} end.";
    REQUIRE(extract_json(input) == "{ { \"key\": \"value\" } and some other text { \"another\": \"object\" }}");
}

TEST_CASE("extract_json extracts the first JSON object when multiple are present") {
    std::string input = "Text before { \"first\": \"value1\" } text in between { \"second\": \"value2\" }";
    REQUIRE(extract_json(input) == "{ \"first\": \"value1\" }");
}