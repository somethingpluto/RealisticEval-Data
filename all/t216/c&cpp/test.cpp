struct MockSubprocessRun {
    std::string stdout_;
    bool check_;

    MockSubprocessRun& operator()(const std::string& command, const std::string& mode) {
        if (command == "ip addr show wlan0" && mode == "r") {
            stdout_ = "3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000\n"
                      "    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic wlan0\n"
                      "       valid_lft 86394sec preferred_lft 86394sec\n";
            check_ = true;
        } else if (command == "ip addr show eth0" && mode == "r") {
            stdout_ = "3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500\n"
                      "    inet 10.0.0.1/24";
            check_ = true;
        } else {
            stdout_ = "";
            check_ = false;
        }
        return *this;
    }
};

// Function to get the local IP address
std::string get_local_ip(const std::string& interface = "wlan0") {
    std::string command = "ip addr show " + interface;
    FILE* pipe = popen(command.c_str(), "r");
    if (!pipe) {
        throw std::runtime_error("Failed to execute command");
    }

    std::string result;
    char buffer[128];
    while (!feof(pipe)) {
        if (fgets(buffer, 128, pipe) != nullptr) {
            result += buffer;
        }
    }
    pclose(pipe);

    // Regular expression to match IPv4 addresses, excluding the loopback address
    std::regex ip_pattern("inet ([0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+)/[0-9]+");

    // Search for IP addresses in the command output
    std::smatch match;
    if (std::regex_search(result, match, ip_pattern)) {
        return match[1];
    } else {
        throw std::runtime_error("No local IP found");
    }
}

TEST_CASE("Test Get Local IP Function", "[get_local_ip]") {
    MockSubprocessRun mock_run;

    SECTION("Successful IP Retrieval") {
        mock_run("ip addr show wlan0", "r").stdout_ = 
            "3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP group default qlen 1000\n"
            "    inet 192.168.1.100/24 brd 192.168.1.255 scope global dynamic wlan0\n"
            "       valid_lft 86394sec preferred_lft 86394sec\n";

        REQUIRE_NOTHROW(get_local_ip("wlan0"));
        REQUIRE(get_local_ip("wlan0") == "192.168.1.100");
    }

    SECTION("Command Failure") {
        mock_run("ip addr show wlan0", "r").check_ = false;

        REQUIRE_THROWS_AS(get_local_ip("wlan0"), std::runtime_error);
    }

    SECTION("Different Interface") {
        mock_run("ip addr show eth0", "r").stdout_ = 
            "3: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500\n"
            "    inet 10.0.0.1/24";

        REQUIRE_NOTHROW(get_local_ip("eth0"));
        REQUIRE(get_local_ip("eth0") == "10.0.0.1");
    }
}