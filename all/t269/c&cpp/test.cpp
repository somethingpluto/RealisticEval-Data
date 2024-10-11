TEST_CASE("Check valid IP addresses", "[ip]") {
    REQUIRE(isCompliantIP("192.168.1.1") == true);
    REQUIRE(isCompliantIP("0.0.0.0") == true);
    REQUIRE(isCompliantIP("255.255.255.255") == true);
}

TEST_CASE("Check invalid IP addresses", "[ip]") {
    REQUIRE(isCompliantIP("256.256.256.256") == false);
    REQUIRE(isCompliantIP("192.168.1") == false);
    REQUIRE(isCompliantIP("192.168.1.256") == false);
    REQUIRE(isCompliantIP("abc.def.ghi.jkl") == false);
    REQUIRE(isCompliantIP("192.168.1.-1") == false);
    REQUIRE(isCompliantIP("192.168.1.0.0") == false);
}