TEST_CASE("Test extract_sld_tld function") {
    SECTION("Test a typical FQDN") {
        REQUIRE(extract_sld_tld("www.example.com") == std::make_pair("example", "com"));
    }

    SECTION("Test another typical FQDN") {
        REQUIRE(extract_sld_tld("www.example.xyz") == std::make_pair("example", "xyz"));
    }

    SECTION("Test an FQDN with multiple subdomains") {
        REQUIRE(extract_sld_tld("blog.subdomain.example.com") == std::make_pair("example", "com"));
    }

    SECTION("Test a numeric TLD") {
        REQUIRE(extract_sld_tld("server.example.123") == std::make_pair("example", "123"));
    }
}