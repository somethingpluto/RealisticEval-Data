TEST_CASE("get_local_ip", "[network]") {
    SECTION("Default interface") {
        std::string result = get_local_ip();
        REQUIRE(result != "No IP found");
        std::cout << "Default interface IP: " << result << std::endl;
    }

    SECTION("Specific interface") {
        std::string result = get_local_ip("eth0");
        REQUIRE(result != "No IP found");
        std::cout << "Specific interface IP: " << result << std::endl;
    }
}