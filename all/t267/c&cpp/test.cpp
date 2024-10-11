TEST_CASE("Extract SLD and TLD", "[extract_sld_tld]") {
    SECTION("Basic Test Case") {
        auto [sld, tld] = extract_sld_tld("example.com");
        REQUIRE(sld == "example");
        REQUIRE(tld == "com");
    }

    SECTION("Subdomain Test Case") {
        auto [sld, tld] = extract_sld_tld("sub.example.co.uk");
        REQUIRE(sld == "sub.example");
        REQUIRE(tld == "co.uk");
    }

    SECTION("Multiple Subdomains Test Case") {
        auto [sld, tld] = extract_sld_tld("level1.level2.sub.example.net");
        REQUIRE(sld == "level1.level2.sub.example");
        REQUIRE(tld == "net");
    }

    SECTION("Top-Level Domain with Hyphen") {
        auto [sld, tld] = extract_sld_tld("example-domain.com");
        REQUIRE(sld == "example-domain");
        REQUIRE(tld == "com");
    }

    SECTION("Single Label Domain") {
        auto [sld, tld] = extract_sld_tld("example");
        REQUIRE(sld.empty());
        REQUIRE(tld == "example");
    }
}