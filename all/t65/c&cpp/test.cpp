TEST_CASE("Find Duplicate IPs", "[find_duplicate_ips]") {
    // Test Case 1: No duplicates and no ignore list
    SECTION("No Duplicates and No Ignore List") {
        std::vector<std::string> ip_list = {"192.168.1.1", "10.0.0.1", "172.16.0.1"};
        std::vector<std::string> ignore_list = {};
        std::vector<std::string> expected_result = {};
        REQUIRE(find_duplicate_ips(ip_list, ignore_list) == expected_result);
    }

    // Test Case 2: Duplicates but all ignored
    SECTION("Duplicates but All Ignored") {
        std::vector<std::string> ip_list = {"192.168.1.1", "192.168.1.1", "10.0.0.1"};
        std::vector<std::string> ignore_list = {"192.168.1.1"};
        std::vector<std::string> expected_result = {};
        REQUIRE(find_duplicate_ips(ip_list, ignore_list) == expected_result);
    }

    // Test Case 3: Single IP with multiple duplicates but one ignored
    SECTION("Single IP with Multiple Duplicates but One Ignored") {
        std::vector<std::string> ip_list = {"192.168.1.1", "192.168.1.1", "192.168.1.1"};
        std::vector<std::string> ignore_list = {"192.168.1.1"};
        std::vector<std::string> expected_result = {};
        REQUIRE(find_duplicate_ips(ip_list, ignore_list) == expected_result);
    }

    // Test Case 4: Multiple IPs with some duplicates and some ignored
    SECTION("Multiple IPs with Some Duplicates and Some Ignored") {
        std::vector<std::string> ip_list = {"192.168.1.1", "192.168.1.1", "10.0.0.1", "10.0.0.1", "172.16.0.1"};
        std::vector<std::string> ignore_list = {"192.168.1.1"};
        std::vector<std::string> expected_result = {"10.0.0.1"};
        REQUIRE(find_duplicate_ips(ip_list, ignore_list) == expected_result);
    }
}