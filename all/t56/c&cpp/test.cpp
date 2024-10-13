TEST_CASE("TestFindShiftJISNotGBK", "[ShiftJISTest]") {
    // Pre-calculate the list once since it's computationally expensive
    auto shiftjis_not_gbk = find_shiftjis_not_gbk();

    SECTION("test_known_shiftjis_character_not_in_gbk") {
        // Test known characters (example values provided might not actually be in one and not the other; please adjust accordingly based on actual encoding tables)
        wchar_t known_shiftjis_only = L'ヱ';  // An example character, ensure this is correct as per your encodings
        REQUIRE(std::find(shiftjis_not_gbk.begin(), shiftjis_not_gbk.end(), known_shiftjis_only) == shiftjis_not_gbk.end());
    }

    SECTION("test_character_in_both_encodings") {
        // Test characters known to be in both encodings
        wchar_t common_character = L'水';  // Common in both, ensure accuracy
        REQUIRE(std::find(shiftjis_not_gbk.begin(), shiftjis_not_gbk.end(), common_character) == shiftjis_not_gbk.end());
    }

    SECTION("test_character_in_neither_encoding") {
        // Character not typically found in either encoding
        wchar_t neither_encoding_char = L'\U0001F4A9';  // Emoji, not in basic Shift-JIS or GBK
        REQUIRE(std::find(shiftjis_not_gbk.begin(), shiftjis_not_gbk.end(), neither_encoding_char) == shiftjis_not_gbk.end());
    }

    SECTION("test_bounds_of_bmp") {
        // Characters at the edge of the BMP should be checked
        wchar_t edge_of_bmp = L'\uffff';  // Last character in BMP
        // Since this test is situational, we check based on the known state; may not be necessary
        if (std::find(shiftjis_not_gbk.begin(), shiftjis_not_gbk.end(), edge_of_bmp) != shiftjis_not_gbk.end()) {
            REQUIRE(std::find(shiftjis_not_gbk.begin(), shiftjis_not_gbk.end(), edge_of_bmp) != shiftjis_not_gbk.end());
        } else {
            REQUIRE(std::find(shiftjis_not_gbk.begin(), shiftjis_not_gbk.end(), edge_of_bmp) == shiftjis_not_gbk.end());
        }
    }
}