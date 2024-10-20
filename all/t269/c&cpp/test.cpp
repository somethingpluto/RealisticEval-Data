TEST_CASE("Test IsCompliantIP", "[is_compliant_ip]") {
    SECTION("Private IP") {
        // Test that private IPs return True
        REQUIRE(is_compliant_ip("192.168.1.1"));
    }

    SECTION("Public IP") {
        // Test that public IPs return False
        REQUIRE_FALSE(is_compliant_ip("8.8.8.8"));
    }

    SECTION("Invalid IP") {
        // Test that invalid IP strings return False
        REQUIRE_FALSE(is_compliant_ip("999.999.999.999"));
    }
}