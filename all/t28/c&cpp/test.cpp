TEST_CASE("TestPrintMemoryBits", "[print_memory_bits]") {
    struct RedirectStdout {
        std::streambuf* orig;
        std::stringstream buffer;

        RedirectStdout() : orig(std::cout.rdbuf(buffer.rdbuf())) {}
        ~RedirectStdout() { std::cout.rdbuf(orig); }

        std::string str() const { return buffer.str(); }
    };

    SECTION("test_single_byte") {
        std::vector<uint8_t> memory_section = {0b10101010};
        RedirectStdout redirector;
        print_memory_bits(memory_section);
        std::string output = redirector.str().substr(0, 8); // Remove newline
        REQUIRE(output == "10101010");
    }

    SECTION("test_multiple_bytes") {
        std::vector<uint8_t> memory_section = {0b11001100, 0b11110000};
        RedirectStdout redirector;
        print_memory_bits(memory_section);
        std::string output = redirector.str();
        REQUIRE(output == "11001100\n11110000\n");
    }

    SECTION("test_all_zeros") {
        std::vector<uint8_t> memory_section = {0b00000000};
        RedirectStdout redirector;
        print_memory_bits(memory_section);
        std::string output = redirector.str().substr(0, 8); // Remove newline
        REQUIRE(output == "00000000");
    }

    SECTION("test_all_ones") {
        std::vector<uint8_t> memory_section = {0b11111111};
        RedirectStdout redirector;
        print_memory_bits(memory_section);
        std::string output = redirector.str().substr(0, 8); // Remove newline
        REQUIRE(output == "11111111");
    }
}