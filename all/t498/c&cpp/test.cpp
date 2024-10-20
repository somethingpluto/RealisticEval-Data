TEST_CASE("Test Compute MD5") {
    SECTION("Test the MD5 hash of an empty string") {
        REQUIRE(compute_md5("") == "d41d8cd98f00b204e9800998ecf8427e");
    }

    SECTION("Test the MD5 hash of a simple string") {
        REQUIRE(compute_md5("Hello, World!") == "65a8e27d8879283831b664bd8b7f0ad4");
    }

    SECTION("Test the MD5 hash of a numeric string") {
        REQUIRE(compute_md5("123456") == "e10adc3949ba59abbe56e057f20f883e");
    }

    SECTION("Test the MD5 hash of a string with special characters") {
        REQUIRE(compute_md5("!@#$%^&*()") == "05b28d17a7b6e7024b6e5d8cc43a8bf7");
    }

    SECTION("Test the MD5 hash of a long string") {
        std::string long_string(1000, 'a');
        std::string expected_hash = "cabe45dcc9ae5b66ba86600cca6b8ba8";
        REQUIRE(compute_md5(long_string) == expected_hash);
    }
}