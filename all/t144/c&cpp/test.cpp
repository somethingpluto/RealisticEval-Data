TEST_CASE("arabicToEnglishNumbers", "[conversion]") {
    SECTION("converts single Arabic numerals to English") {
        REQUIRE(arabicToEnglishNumbers("١") == "1");
        REQUIRE(arabicToEnglishNumbers("٥") == "5");
        REQUIRE(arabicToEnglishNumbers("٩") == "9");
    }

    SECTION("converts a string of Arabic numerals to English") {
        REQUIRE(arabicToEnglishNumbers("٠١٢٣٤٥٦٧٨٩") == "0123456789");
    }

    SECTION("handles strings with Arabic and English numerals mixed") {
        REQUIRE(arabicToEnglishNumbers("٠١23٤5") == "012345");
    }

    SECTION("leaves non-numeral characters unchanged") {
        REQUIRE(arabicToEnglishNumbers("Hello World!") == "Hello World!");
        REQUIRE(arabicToEnglishNumbers("2022-٢٠٢٣") == "2022-2023");
    }

    SECTION("works with full sentences that include Arabic numerals") {
        REQUIRE(arabicToEnglishNumbers("The year is ٢٠٢٤!") == "The year is 2024!");
    }

    SECTION("handles empty strings correctly") {
        REQUIRE(arabicToEnglishNumbers("") == "");
    }

    SECTION("processes Arabic numerals in a complex mixed context") {
        REQUIRE(arabicToEnglishNumbers("Price: ٥٠٠$ and Date: ٢٠٢٣-١٢-٠١") == "Price: 500$ and Date: 2023-12-01");
    }
}