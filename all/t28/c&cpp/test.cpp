class OutputCapture {
public:
    OutputCapture() {
        // Redirect stdout to a stringstream
        old_buf = std::cout.rdbuf(buffer.rdbuf());
    }

    ~OutputCapture() {
        // Restore stdout
        std::cout.rdbuf(old_buf);
    }

    std::string str() const {
        return buffer.str();
    }

private:
    std::stringstream buffer;
    std::streambuf* old_buf;
};
TEST_CASE("Test print_memory_bits function") {
    // Test case for a single byte
    SECTION("Single byte") {
        OutputCapture capture;
        std::vector<unsigned char> memory_section = {0b10101010};
        print_memory_bits(memory_section);
        REQUIRE(capture.str() == "10101010\n");
    }

    // Test case for multiple bytes
    SECTION("Multiple bytes") {
        OutputCapture capture;
        std::vector<unsigned char> memory_section = {0b11001100, 0b11110000};
        print_memory_bits(memory_section);
        REQUIRE(capture.str() == "11001100\n11110000\n");
    }

    // Test case for all zeros
    SECTION("All zeros") {
        OutputCapture capture;
        std::vector<unsigned char> memory_section = {0b00000000};
        print_memory_bits(memory_section);
        REQUIRE(capture.str() == "00000000\n");
    }

    // Test case for all ones
    SECTION("All ones") {
        OutputCapture capture;
        std::vector<unsigned char> memory_section = {0b11111111};
        print_memory_bits(memory_section);
        REQUIRE(capture.str() == "11111111\n");
    }
}