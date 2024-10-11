TEST_CASE("Valid POST request line", "[parse_http_request_line]") {
    std::string response = "POST /api/data HTTP/1.1\r\n";
    auto parsed_info = parse_http_request_line(response);

    REQUIRE(parsed_info["method"] == "POST");
    REQUIRE(parsed_info["url"] == "/api/data");
    REQUIRE(parsed_info["http_version"] == "HTTP/1.1");
}

TEST_CASE("PUT request line", "[parse_http_request_line]") {
    std::string response = "PUT /api/update HTTP/2.0\r\n";
    auto parsed_info = parse_http_request_line(response);

    REQUIRE(parsed_info["method"] == "PUT");
    REQUIRE(parsed_info["url"] == "/api/update");
    REQUIRE(parsed_info["http_version"] == "HTTP/2.0");
}

TEST_CASE("DELETE request line", "[parse_http_request_line]") {
    std::string response = "DELETE /api/delete HTTP/1.1\r\n";
    auto parsed_info = parse_http_request_line(response);

    REQUIRE(parsed_info["method"] == "DELETE");
    REQUIRE(parsed_info["url"] == "/api/delete");
    REQUIRE(parsed_info["http_version"] == "HTTP/1.1");
}

TEST_CASE("Malformed request line", "[parse_http_request_line]") {
    std::string response = "INVALID REQUEST LINE\r\n";
    auto parsed_info = parse_http_request_line(response);

    REQUIRE(parsed_info.empty());  // Expect empty result for malformed request
}