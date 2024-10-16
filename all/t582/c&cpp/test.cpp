TEST_CASE("toQueryString") {
    SECTION("should convert a simple object to a query string") {
        std::map<std::string, std::string> params = {{"search", "test"}, {"page", "1"}, {"size", "10"}};
        std::string result = toQueryString(params);
        REQUIRE(result == "?search=test&page=1&size=10");
    }

    SECTION("should encode special characters in the query string") {
        std::map<std::string, std::string> params = {{"search", "hello world"}, {"filter", "price < $50"}};
        std::string result = toQueryString(params);
        REQUIRE(result == "?search=hello%20world&filter=price%20%3C%20%2450");
    }

    SECTION("should handle empty string values") {
        std::map<std::string, std::string> params = {{"search", ""}, {"page", "1"}};
        std::string result = toQueryString(params);
        REQUIRE(result == "?search=&page=1");
    }

    SECTION("should handle boolean values") {
        std::map<std::string, std::string> params = {{"isActive", "true"}, {"isVerified", "false"}};
        std::string result = toQueryString(params);
        REQUIRE(result == "?isActive=true&isVerified=false");
    }
}