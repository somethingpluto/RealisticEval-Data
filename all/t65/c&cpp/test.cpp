TEST_CASE("Test findDuplicateIPs function") {
    SECTION("Basic duplicates") {
        std::vector<std::string> ipList = {"192.168.1.1", "192.168.1.2", "192.168.1.1"};
        std::vector<std::string> ignoreList = {};
        REQUIRE(findDuplicateIPs(ipList, ignoreList) == std::vector<std::string>({"192.168.1.1"}));
    }

    SECTION("Ignored duplicates") {
        std::vector<std::string> ipList = {"192.168.1.1", "192.168.1.1", "192.168.1.2"};
        std::vector<std::string> ignoreList = {"192.168.1.1"};
        REQUIRE(findDuplicateIPs(ipList, ignoreList).empty());
    }

    SECTION("No duplicates") {
        std::vector<std::string> ipList = {"192.168.1.1", "192.168.1.2", "192.168.1.3"};
        std::vector<std::string> ignoreList = {};
        REQUIRE(findDuplicateIPs(ipList, ignoreList).empty());
    }

    SECTION("Mixed duplicates") {
        std::vector<std::string> ipList = {"192.168.1.1", "192.168.1.1", "10.0.0.1", "192.168.1.2"};
        std::vector<std::string> ignoreList = {"192.168.1.2"};
        REQUIRE(findDuplicateIPs(ipList, ignoreList) == std::vector<std::string>({"192.168.1.1"}));
    }

    SECTION("Empty input") {
        std::vector<std::string> ipList = {};
        std::vector<std::string> ignoreList = {};
        REQUIRE(findDuplicateIPs(ipList, ignoreList).empty());
    }

    SECTION("Only ignored IPs") {
        std::vector<std::string> ipList = {"192.168.1.1", "192.168.1.1"};
        std::vector<std::string> ignoreList = {"192.168.1.1"};
        REQUIRE(findDuplicateIPs(ipList, ignoreList).empty());
    }

    SECTION("All duplicates") {
        std::vector<std::string> ipList = {"192.168.1.1", "192.168.1.1", "192.168.1.1"};
        std::vector<std::string> ignoreList = {};
        REQUIRE(findDuplicateIPs(ipList, ignoreList) == std::vector<std::string>({"192.168.1.1"}));
    }
}