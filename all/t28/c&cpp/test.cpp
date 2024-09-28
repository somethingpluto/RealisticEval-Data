#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include <iostream>
#include <sstream>
#include <vector>
#include <cstdint>

void print_memory_bits(const std::vector<uint8_t>& memory_section) {
    for (size_t byte_index = 0; byte_index < memory_section.size(); ++byte_index) {
        std::cout << "Byte " << byte_index << ": ";
        uint8_t byte = memory_section[byte_index];
        
        for (int bit_index = 7; bit_index >= 0; --bit_index) {
            // Shift the bit to the right and check the least significant bit
            int bit_status = (byte >> bit_index) & 1;
            std::cout << bit_status << " ";
        }
        std::cout << std::endl;  // Newline after each byte
    }
}

TEST_CASE("Single byte is printed correctly", "[print_memory_bits]") {
    std::vector<uint8_t> memory_section = {0b10101010};
    
    std::ostringstream buffer;
    std::streambuf* prevcoutbuf = std::cout.rdbuf(buffer.rdbuf());  // Redirect cout to buffer
    
    print_memory_bits(memory_section);
    
    std::string output = buffer.str();
    std::cout.rdbuf(prevcoutbuf);  // Restore original stream buffer
    std::string expected_output = "Byte 0: 1 0 1 0 1 0 1 0 \n";
    REQUIRE(output == expected_output);
}

TEST_CASE("Multiple bytes are printed correctly", "[print_memory_bits]") {
    std::vector<uint8_t> memory_section = {0b11001100, 0b11110000};
    
    std::ostringstream buffer;
    std::streambuf* prevcoutbuf = std::cout.rdbuf(buffer.rdbuf());  // Redirect cout to buffer
    
    print_memory_bits(memory_section);
    
    std::string output = buffer.str();
    std::cout.rdbuf(prevcoutbuf);  // Restore original stream buffer
    std::string expected_output = "Byte 0: 1 1 0 0 1 1 0 0 \nByte 1: 1 1 1 1 0 0 0 0 \n";
    REQUIRE(output == expected_output);
}

TEST_CASE("All zeros byte is printed correctly", "[print_memory_bits]") {
    std::vector<uint8_t> memory_section = {0b00000000};
    
    std::ostringstream buffer;
    std::streambuf* prevcoutbuf = std::cout.rdbuf(buffer.rdbuf());  // Redirect cout to buffer
    
    print_memory_bits(memory_section);
    
    std::string output = buffer.str();
    std::cout.rdbuf(prevcoutbuf);  // Restore original stream buffer
    std::string expected_output = "Byte 0: 0 0 0 0 0 0 0 0 \n";
    REQUIRE(output == expected_output);
}

TEST_CASE("All ones byte is printed correctly", "[print_memory_bits]") {
    std::vector<uint8_t> memory_section = {0b11111111};
    
    std::ostringstream buffer;
    std::streambuf* prevcoutbuf = std::cout.rdbuf(buffer.rdbuf());  // Redirect cout to buffer
    
    print_memory_bits(memory_section);
    
    std::string output = buffer.str();
    std::cout.rdbuf(prevcoutbuf);  // Restore original stream buffer
    std::string expected_output = "Byte 0: 1 1 1 1 1 1 1 1 \n";
    REQUIRE(output == expected_output);
}

TEST_CASE("Mixed bytes are printed correctly", "[print_memory_bits]") {
    std::vector<uint8_t> memory_section = {0b01010101, 0b10000001};
    
    std::ostringstream buffer;
    std::streambuf* prevcoutbuf = std::cout.rdbuf(buffer.rdbuf());  // Redirect cout to buffer
    
    print_memory_bits(memory_section);
    
    std::string output = buffer.str();
    std::cout.rdbuf(prevcoutbuf);  // Restore original stream buffer
    std::string expected_output = "Byte 0: 0 1 0 1 0 1 0 1 \nByte 1: 1 0 0 0 0 0 0 1 \n";
    REQUIRE(output == expected_output);
}