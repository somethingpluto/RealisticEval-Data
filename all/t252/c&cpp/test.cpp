TEST_CASE("Bit conversion", "[bitsequenceencoder]") {
    BitSequenceEncoder encoder;
    json data = {{"bits", 255}};
    std::string encoded_data = encoder.encode(data);
    std::string expected_output = R"({"bits": "11111111"})";
    REQUIRE(encoded_data == expected_output);
}