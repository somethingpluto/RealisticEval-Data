// Test cases
TEST_CASE("Valid HTTP request line", "[parse_http_request_line]") {
    std::string response = "GET /index.html HTTP/1.1\r\n";
    auto parsed_info = parse_http_request_line(response);

    REQUIRE(parsed_info["method"] == "GET");
    REQUIRE(parsed_info["url"] == "/index.html");
    REQUIRE(parsed_info["http_version"] == "HTTP/1.1");
}

TEST_CASE("Valid POST request line", "[parse_http_request_line]") {
    std::string response = "POST /api/data HTTP/1.1\r\n";
    auto parsed_info = parse_http_request_line(response);

    REQUIRE(parsed_info["method"] == "POST");
    REQUIRE(parsed_info["url"] == "/api/data");
    REQUIRE(parsed_info["http_version"] == "HTTP/1.1");
}

TEST_CASE("Request line without HTTP version", "[parse_http_request_line]") {
    std::string response = "PUT /upload\r\n";
    auto parsed_info = parse_http_request_line(response);

    REQUIRE(parsed_info["method"] == "PUT");
    REQUIRE(parsed_info["url"] == "/upload");
    REQUIRE(parsed_info["http_version"].empty());
}

TEST_CASE("Request line with extra spaces", "[parse_http_request_line]") {
    std::string response = "  GET   /index.html   HTTP/1.1  \r\n";
    auto parsed_info = parse_http_request_line(response);

    REQUIRE(parsed_info["method"] == "GET");
    REQUIRE(parsed_info["url"] == "/index.html");
    REQUIRE(parsed_info["http_version"] == "HTTP/1.1");
}